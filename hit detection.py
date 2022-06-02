import pickle
import codecs
base64_encoded_board = "gASV9QAAAAAAAABdlChdlChLBUsFSwVLBUsFSwBLAEsASwBLAGVdlChLBEsESwRLBEsASwBLAEsA\nSwBLAGVdlChLA0sDSwNLAEsASwBLAEsASwBLAGVdlChLAksCSwBLAEsASwBLAEsASwBLAGVdlChL\nAUsASwBLAEsASwBLAEsASwBLAGVdlChLAEsASwBLAEsASwBLAEsASwBLAGVdlChLAEsASwBLAEsA\nSwBLAEsASwBLAGVdlChLAEsASwBLAEsASwBLAEsASwBLAGVdlChLAEsASwBLAEsASwBLAEsASwBL\nAGVdlChLAEsASwBLAEsASwBLAEsASwBLAGVlLg==\n"

def pickler(board):
  string_pickle = codecs.encode(pickle.dumps(board), "base64").decode()
  return string_pickle

def unpickler(string_pickle):
  unpickled = pickle.loads(codecs.decode(string_pickle.encode(), "base64"))
  return unpickled

def l2n(coord):
  return [ord(coord[0])-65,int(coord[1])]

def val(coord, board):
  coord = l2n(coord)
  return board[coord[1]][coord[0]]

board = unpickler(base64_encoded_board)

def main():
  coord = input("Coord >>>").upper()
  print(val(coord, board))

if __name__ == "__main__":
  main()