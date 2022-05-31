import requests
obj = {"id":"GAY"}

req = requests.post("http://localhost:5050/post", json=str(obj))


print(req.text)