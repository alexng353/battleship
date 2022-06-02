import requests

import json

mything = json.dumps({"game":"976453"})


req = requests.post("http://localhost:5050/ready", json=(mything))

res = req.json()

print(res)
