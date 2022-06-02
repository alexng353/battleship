import requests
import json
obj = json.dumps({"id":"CHING CHENG HANJI"})

req = requests.post("http://localhost:5050/setboard", json=(obj))


print(req.text)