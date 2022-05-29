import json
from sanic import Sanic
from sanic.response import json as json_response
import uuid
import random

from cors import add_cors_headers
from options import setup_options

import redis

r = redis.Redis(host="localhost", port=6379, db=1)

app = Sanic(name=__name__)

# localhost/new?args=thing
@app.get("/new")
async def new(request):
    user_id = str(uuid.uuid4())
    game_id = random.randint(100000, 999999)

    r.hset(game_id, "p1", user_id)
    r.hset(game_id, "p1-board", "")

    params = {
        "id": user_id,
        "game": game_id,
        "args": request.args,
    }

    return json_response(params)


@app.route("/join")
async def join(request):
    user_id = str(uuid.uuid4())
    game_id = request.args.get("game")
    
    if r.hget(game_id, "p1") and r.hget(game_id, "p2"):
        return json_response({"error": "Game is full"})


    if r.hget(game_id, "p1") == None:
        r.hset(game_id, "p1", user_id)
        r.hset(game_id, "p1-board", "")
    else:
        r.hset(game_id, "p2", user_id)
        r.hset(game_id, "p2-board", "")


    params = {
        "id": user_id,
        "game": game_id,
        "args": request.args,
    }

    return json_response(params)

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
            return json_response(params)
        else:
            return json_response({"error": "You are not the player"})
    else:
        return json_response({"error": "Missing id or game"})
@app.route("/move")
async def move(request):
    
    params = {}
    
    return json_response(params)

app.register_listener(setup_options, "before_server_start")

app.register_middleware(add_cors_headers, "response")

app.run(host="0.0.0.0", workers=4, port=5050, dev=True)