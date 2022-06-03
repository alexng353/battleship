import requests
import json
obj = json.dumps({"game":"654321"})

req = requests.post("http://localhost:5050/ready", json=(obj))


print(req.text)