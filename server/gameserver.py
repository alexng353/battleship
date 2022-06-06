import codecs
import json
import pickle
from sanic import Sanic
from sanic import response
import uuid
import random
import ast

from cors import add_cors_headers
from options import setup_options

import redis

r = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)

app = Sanic(name=__name__)

# localhost/new?args=thing
def pickler(board):
  string_pickle = codecs.encode(pickle.dumps(board), "base64").decode()
  return string_pickle

def unpickler(string_pickle):
  unpickled = pickle.loads(codecs.decode(string_pickle, "base64"))
  return unpickled

def l2n(coord):
  return [ord(coord[0])-65,int(coord[1])]

def val(coord, board):
  coord = l2n(coord)
  return board[coord[1]][coord[0]]

def hitdet(coord, board):
  value = val(coord, board)
  if value == 0:
    return(False)
  if value in [1, 2, 3, 4, 5]:
    return(True)

@app.route("/", methods=["GET"])
async def root(request):
  return response.text("BATTLESHIP")

@app.route("/ready", methods=["POST"])
async def ready(request):
  data = ast.literal_eval(request.json)
  game = data.get("game")

  p1 = r.hget(game, "p1")
  p2 = r.hget(game, "p2")

  ready = False
  if r.hget(game, str(p1)) and r.hget(game, str(p2)):
    ready = True

  return response.json({"ready":ready, "game":game})

@app.route("/update", methods=["POST"])
async def post(request):
  data = ast.literal_eval(request.json)
  game = data.get("game")
  uid = data.get("id")

  return response.text("endpoint")

@app.route("/shoot", methods=["POST"])
async def shoot(request):
  data = ast.literal_eval(request.json)

  game = data.get("game")
  coord = data.get("coord")
  uid = data.get("id")

  p1 = r.hget(game, "p1")
  p2 = r.hget(game, "p2")

  moves = unpickler(r.hget(game, f"{uid}-moves"))

  if p1 == uid:
    victim = r.hget(game, p2)
  else:
    victim = r.hget(game, p1)


  victim = unpickler(victim)
  
  hit = hitdet(coord, victim)

# hopefully this works
  r.hset(game, f"{uid}-moves", pickler(moves.append({coord:hit})))

  return response.json(json.dumps({"game":game, "coord":coord, "hit":hit}))

@app.route("/setboard", methods=["POST"])
async def setboard(request):
  data = json.loads(request.json)
  r.hset(data.get("game"), data.get("id"), data.get("board"))

  return response.text(str({data.get("id"), data.get("board")}))

# @app.route("/hitdet", methods=["POST"])
# async def hitdet(request):
#   data = ast.literal_eval(request.json)

#   shooter = data.get("id")
#   game = data.get("game")

#   coord = data.get("coord")

#   p1 = r.hget(game, "p1")
#   p2 = r.hget(game, "p2")

#   victim = p1 if shooter == p2 else p2
  
#   victim_board = unpickler(r.hget(game, victim))

#   res = hitdet(coord, victim_board)
#   if res == True:


@app.get("/new")
async def new(request):
  user_id = str(uuid.uuid4())
  # anti collision loop
  game_id = random.randint(100000, 999999)

  r.hset(game_id, "p1", user_id)

  params = {
    "id": user_id,
    "game": game_id
  }

  return response.json(params)

@app.route("/join")
async def join(request):
  args = request.args
  try:
    user_id = str(uuid.uuid4())
    game_id = args.get("game")

    if len(game_id) != 6:
      return response.json({"error":"Invalid game code"})
    
    if r.hget(game_id, "p1") and r.hget(game_id, "p2"):
      return response.json({"error": "Game is full"})

    if r.hget(game_id, "p1") == None:
      r.hset(game_id, "p1", user_id)
    else:
      r.hset(game_id, "p2", user_id)

    params = {
      "id": user_id,
      "game": game_id
    }
    
    return response.json(params)

  except Exception as e:
    return response.json({"error": str(e)})



@app.route("/get")
async def get(request):
  args = request.args
  if args["id"] and args["game"]:
    user_id = args["id"]
    game_id = args["game"]
    if r.hget(game_id, "p1") == user_id:
      params = {
        "id": user_id,
        "game": game_id,
        "args": args,
      }
      return response.json(params)
    else:
      return response.json({"error": "You are not the player"})
  else:
    return response.json({"error": "Missing id or game"})
@app.route("/move")
async def move(request):
  
  params = {}
  
  return response.json(params)

app.register_listener(setup_options, "before_server_start")

app.register_middleware(add_cors_headers, "response")

app.run(host="0.0.0.0", workers=4, port=5050, dev=True)
