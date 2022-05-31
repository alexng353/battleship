import codecs
import json
import pickle
import codecs

board = [[5, 5, 5, 5, 5, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [3, 3, 3, 0, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

string_pickle = codecs.encode(pickle.dumps(board), "base64").decode()

unpickled = pickle.loads(codecs.decode(string_pickle.encode(), "base64"))

def pickler(board):
  string_pickle = codecs.encode(pickle.dumps(board), "base64").decode()
  return string_pickle

def unpickler(string_pickle):
  unpickled = pickle.loads(codecs.decode(string_pickle.encode(), "base64"))
  return unpickled

print(type(string_pickle))
print(unpickled)