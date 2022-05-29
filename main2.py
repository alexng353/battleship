import string

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



    self.start_loop()
  
  def l2n(self,coord):
    return [ord(coord[0])-65,int(coord[1])]
  def n2l(self,coord):
    return [chr(coord[0]+65),int(coord[1])]

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
    self.placed_ships[ship] = [start, stop]
    return True

  def valid_coord(self, coord):
    if len(coord) != 2:
      return False
    if not (ord(coord[0]) >= 65 and ord(coord[0]) <= 74):
      return False
    if not (int(coord[1]) >= 0 and int(coord[1]) <= 9):
      return False
    return True


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
    for i in range(10):
      print(f" {i} {self.board[i]}   | {i} {self.enemy_board[i]}")
    print()


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
      elif command == "quit":
        break
      else:
        print("Invalid command.")

  def game_initialize(self):
    
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
        print("Invalid ship")
        continue

      length = self.ships[ship]
      print("Choose a starting coordinate")

      coord = input("Coordinate: ")
      if not self.valid_coord(coord):
        print("Invalid coordinate")
        continue

      if not self.unused_coord(coord):
        print("Coordinate already used")
        continue
      
      if ship != "dingy":
        print("Choose a direction")
        print("l, r, u, d")
        direction = input("Direction: ")
        if direction not in ["l", "r", "u", "d"]:
          print("Invalid direction")
          continue
      else:
        direction = "l"

      stop = self.hyundai(coord, length, direction)
      if not self.valid_coord(stop):
        print("Invalid coordinate")
        continue

      if not self.place_ship(ship, coord, stop):
        print("Invalid ship placement")
        continue

      print("Ship placed")
      self.ship_printer(ship, coord, stop)
      print()
      if len(self.placed_ships) == 5:
        break
    



  def game_loop(self):
    while True:
      break



if __name__ == "__main__":
  game = Game()