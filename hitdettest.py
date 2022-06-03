import requests
import json

obj = json.dumps({
  "game":"123456",
  "coord":"A9",
  "id":"85cabe0b-1b1a-4326-a5e0-7722771dfaeb"
})


req = requests.post("http://localhost:5050/shoot", json=obj)

res = req.json()

print(res)
