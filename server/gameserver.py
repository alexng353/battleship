import json
from sanic import Sanic
from sanic.response import json as json_response
import uuid

from cors import add_cors_headers
from options import setup_options

import redis

r = redis.Redis(host='localhost', port=6379, db=1)

app = Sanic(name=__name__)


@app.get('/game')
async def root(request):
    new = False
    try:
        new = request.args["new"]
    except:
        print("Cry about it")

    params = {
        "id":uuid.uuid4(),
        "args":request.args,
        "new":new
    }

    return json_response(params)



app.register_listener(setup_options, "before_server_start")

app.register_middleware(add_cors_headers, "response")

app.run(host='0.0.0.0', workers=4, port=5050, dev=True)