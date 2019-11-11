'''
    This is an information API which actually is written using quart library.
    This would accept request and respond to that request asynchronously.
'''

import json
import asyncio
import uuid
from quart import Quart, render_template

from Util import *

app = Quart("Information Service")

@app.route('/info',methods=['GET'])
async def getInformation():

    print(Util.getLogTimeStamp(), "Inside in getInformation()")
    requestCorrelationId = str(uuid.uuid4())

    print(Util.getLogTimeStamp(), "Received request ::[" + requestCorrelationId+"]")

    await __doProcessing()

    result = json.dumps({"result": "success","id" : str(requestCorrelationId)})

    print(Util.getLogTimeStamp(), "Sending Response ::["+ result + "]")

    return result

async def __doProcessing():

    print(Util.getLogTimeStamp(), "Inside in __doProcessing()")
    await asyncio.sleep(5)

if __name__ == "__main__":
    app.run('0.0.0.0', 8000)
    print(Util.getLogTimeStamp(), "Info api has been started and listening on http://0.0.0.0:8000/info")