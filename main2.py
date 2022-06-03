import codecs
import json
import pickle
import string
import requests
import time

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  SHIP = '\033[48;5;11m'
  HIT = '\033[48;5;10m'
  MISS = '\033[48;5;9m'
  HITME = '\033[48;5;9m'
  SUNK = '\033[48;5;16m'

class Game():
  def __init__(self):
    self.board = [[0 for i in range(10)] for i in range(10)]
    
    self.enemy_board = [[0 for i in range(10)] for i in range(10)]
    self.ships = {
      "carrier": 4,
      "battleship": 3,
      "cruiser": 2,
      "destroyer": 1,
      "dingy": 0
    }
    self.ready = False
    self.enemy_ready = False

    # carrier: [A2, A6]
    self.placed_ships = {}
    
    self.enemy_shots = []
    self.shots = []

    self.url = "http://localhost:5050"

    

    self.start_loop()
  
  def warn(self, msg):
    print(bcolors.FAIL + msg + bcolors.ENDC)

  def l2n(self,coord):
    return [ord(coord[0])-65,int(coord[1])]

  def n2l(self,coord):
    return [chr(coord[0]+65),int(coord[1])]
    
  def pickler(self, board):
    string_pickle = codecs.encode(pickle.dumps(board), "base64").decode()
    return string_pickle

  def unpickler(self, string_pickle):
    unpickled = pickle.loads(codecs.decode(string_pickle, "base64"))
    return unpickled
    
  def key(self):
    print(r"""
    KEY FOR YOUR BOARD:
    0: No battleship
    1-5: battleship of n length
    8: hit
    9: sunk

    KEY FOR OPPONENTS BOARD:
    0: unknown
    8: hit
    9: sink
    """)
  
  def get_value(self, coord):
    coord = self.l2n(coord)
    return self.board[coord[1]][coord[0]]

  def ship_printer(self, ship, start, stop):
    # print(start, stop)
    start = self.l2n(start)
    stop = self.l2n(stop)
    # print(start,stop)

    # check to make sure the ship is going right or down
    # if the ship is going left or up, reverse the start and stop
    if start[0] > stop[0] or start[1] > stop[1]:
      start, stop = stop, start

    # code below works for down and right directions
    for i in range(start[0],stop[0]+1):
      for j in range(start[1],stop[1]+1):
        self.board[j][i] = self.ships.get(ship)+1

  def place_ship(self, ship, start, stop):
    if self.check_intersect(start, stop):
      self.warn("Ship intersects with another ship.")
      return False
    self.placed_ships[ship] = [start, stop]
    return True

  def valid_coord(self, coord):
    try:
      if len(coord) != 2:
        return False
      if not (ord(coord[0]) >= 65 and ord(coord[0]) <= 74):
        return False
      if not (int(coord[1]) >= 0 and int(coord[1]) <= 9):
        return False
      return True
    except: return False

  def unused_coord(self, coord):
    coord = self.l2n(coord)
    if self.board[coord[1]][coord[0]] == 0:
      return True
    return False

  def hyundai(self, coord, length, direction):
    if direction == "l":
      # move left by length spaces
      return chr(ord(coord[0])-length) + coord[1]
    elif direction == "r":
      # move right by length spaces
      return chr(ord(coord[0])+length) + coord[1]
    elif direction == "u":
      # move up by length spaces
      return coord[0] + str(int(coord[1])-length)
    elif direction == "d":
      # move down by length spaces
      return coord[0] + str(int(coord[1])+length)
    else:
      return None

  def print_board(self):
    letters = "  ".join(list(string.ascii_uppercase)[:10])
    print()
    print(f'    YOUR BOARD                      |    OPPONENT\'S BOARD')
    print(f'    {letters}    |    {letters}')

    board = []

    for i in range(10):
      row = []
      for j in range(10):
        if self.board[i][j] == 0:
          row.append("0, ")
        elif self.board[i][j] == 8:
          row.append(f"{bcolors.HITME}8, {bcolors.ENDC}")
        else:
          row.append(f"{bcolors.SHIP}{self.board[i][j]}, {bcolors.ENDC}")
      board.append(row)

    enemy = []
    for i in range(10):
      row = []
      for j in range(10):
        if self.enemy_board[i][j] == 0:
          row.append("0, ")
        elif self.enemy_board[i][j] == 8:
          row.append(f"{bcolors.HIT}{self.enemy_board[i][j]}, {bcolors.ENDC}")
        else:
          row.append(f"{bcolors.SHIP}{self.enemy_board[i][j]}, {bcolors.ENDC}")
      enemy.append(row)

    for i in range(10):
      print(i, end="  [")
      for j in range(10):
        print(f"{board[i][j]}", end="")
      print(f"\b\b]   | {i} [", end="")
      for j in range(10):
        print(f"{enemy[j][i]}", end="")
      print(f"\b\b]")

    # for i in range(10):
    #   print(f" {i} {self.board[i]}   | {i} {self.enemy_board[i]}")
    print()

  def check_intersect(self, start, stop):
    # print(start, stop)
    start = self.l2n(start)
    stop = self.l2n(stop)
    # check to make sure the ship is going right or down
    # if the ship is going left or up, reverse the start and stop
    if start[0] > stop[0] or start[1] > stop[1]:
      start, stop = stop, start

    # code below works for down and right directions
    checked = []
    for i in range(start[0],stop[0]+1):
      for j in range(start[1],stop[1]+1):
        checked.append(self.board[j][i])

    if any(x in checked for x in [1,2,3,4,5]):
      return(True)
    else:
      return(False)

  def start_loop(self):
    while True:
      print("""
        Welcome to Battleship!
        Enter 'new' to start a new game.
        Enter 'quit' to quit.
        """)
      command = input("Command: ")
      if command == "new":
        self.game_initialize()
        break
      if command == "join":
        tmp = input("Server >>> ")
        if len(tmp) != 6:
          print("Invalid server code.")
          continue
        self.game_initialize(tmp)
        break
      elif command == "quit":
        break
      else:
        print("Invalid command.")

  def game_initialize(self, server=None):
    if server:
      req = requests.get(f"{self.url}/join?game={server}")
      res = req.json()
    else:
      req = requests.get(f"{self.url}/new")
      res = req.json()

    self.id=res.get("id")
    self.gamecode=res.get("game")
    
    print("game code: " + self.gamecode)

    while True:
      self.print_board()
      print("Choose a ship to place")
      for ship, length in self.ships.items():
        if ship not in self.placed_ships:
          print(f"{ship}: {length+1}")

      if len(self.placed_ships) > 0:
        print("\nPlaced ships:")
      for ship in self.placed_ships.keys():
        print(f"{ship}")

      print()

      ship = input("Ship: ")
      if ship not in self.ships:          
        self.warn("Invalid ship")
        continue

      if ship in self.placed_ships:
        self.warn(f"You placed \"{ship}\" already")
        continue

      length = self.ships[ship]
      print("Choose a starting coordinate")

      coord = input("Coordinate: ").upper()
      if not self.valid_coord(coord):
        self.warn("Invalid coordinate")
        continue

      if not self.unused_coord(coord):
        self.warn("Invalid Location")
        continue

      
      if ship != "dingy":
        print("Choose a direction")
        print("l, r, u, d")
        direction = input("Direction: ")
        if direction not in ["l", "r", "u", "d"]:
          self.warn("Invalid direction")
          continue
      else:
        direction = "l"

      stop = self.hyundai(coord, length, direction)
      if not self.valid_coord(stop):
        self.warn("Invalid coordinate")
        continue

      if not self.place_ship(ship, coord, stop):
        self.warn("Invalid ship placement")
        continue

      print("Ship placed")
      self.ship_printer(ship, coord, stop)
      print(coord)
      print(stop)
      print()
      if len(self.placed_ships) == 5:
        data = json.dumps({"id": self.id, "game": self.gamecode, "board": self.pickler(self.board)})
        req = requests.post(f"{self.url}/setboard", json=(data))
        res = req.text

        print(res)
        self.wait_loop()
        break

  def wait_loop(self):
    # data = {
    #   "id":uid,
    #   "game":gamecode
    # }
    # req = requests.post(f"{self.url}/ready", json=(data))
    print(self.id)
    print(self.gamecode)

    while True:
      req = requests.post(f"{self.url}/ready", json=(json.dumps({"game":str(self.gamecode)})))
      res = req.json()

      if res.get("ready") == "True":
        print("wow")
        self.game_loop()
        break
      print("not ready" + str(res))
      time.sleep(3)
      pass
    
  def game_loop():
    pass


if __name__ == "__main__":
  game = Game()