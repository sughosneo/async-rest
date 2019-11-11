'''
    This is an information API which actually is written using aiohttp library.
    This would accept request and respond to that request asynchronously.
'''
from aiohttp import web
import uuid
import json
import asyncio

from Util import *

async def getInformation(request):

    requestCorrelationId = str(uuid.uuid4())

    print(Util.getLogTimeStamp(),"Received request ::[" + requestCorrelationId + "]")

    await asyncio.sleep(5)

    result = {"result": "success", "id": str(requestCorrelationId)}

    print(Util.getLogTimeStamp(),"Sending Response ::[" + json.dumps(result) + "]")

    return web.json_response(result)

app = web.Application()
app.add_routes([web.get('/info', getInformation)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)