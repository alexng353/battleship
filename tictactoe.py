class Game():
  def __init__(self):
    self.board = [["☐" for i in range(3)] for i in range(3)]
    self.board_printer()

  def board_printer(self):
    for i in range(3):
      print(" ".join(self.board[i]))
        
        


if __name__ == "__main__":
  game = Game()