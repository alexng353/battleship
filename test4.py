import redis
import codecs
import pickle
import json

r = redis.Redis(host="localhost", port=6379, db=1)

def pickler(board):
  string_pickle = codecs.encode(pickle.dumps(board), "base64").decode()
  return string_pickle

def unpickler(string_pickle):
  unpickled = pickle.loads(codecs.decode(string_pickle))
  return unpickled

data = r.hget("149510", "0b33f749-817c-481f-9b2b-904d142ee8fe")
print(pickle.loads(codecs.decode(data, "base64")))

# pickled = 'gASV9QAAAAAAAABdlChdlChLBUsFSwVLBUsFSwBLAEsASwBLAGVdlChLBEsESwRLBEsASwBLAEsA\nSwBLAGVdlChLA0sDSwNLAEsASwBLAEsASwBLAGVdlChLAksCSwBLAEsASwBLAEsASwBLAGVdlChL\nAUsASwBLAEsASwBLAEsASwBLAGVdlChLAEsASwBLAEsASwBLAEsASwBLAGVdlChLAEsASwBLAEsA\nSwBLAEsASwBLAGVdlChLAEsASwBLAEsASwBLAEsASwBLAGVdlChLAEsASwBLAEsASwBLAEsASwBL\nAGVdlChLAEsASwBLAEsASwBLAEsASwBLAGVlLg==\n'
# print(unpickler(pickled))



# print(unpickler(r.hget("149510", "0b33f749-817c-481f-9b2b-904d142ee8fe")))
# print(type(r.hget("149510", "0b33f749-817c-481f-9b2b-904d142ee8fe")))
# print(r.hget("149510", "0b33f749-817c-481f-9b2b-904d142ee8fe"))

# print(pickle.loads(r.hget("583102", "def7d536-f6e4-48b9-a66e-e5c508c5d18a")))