import asyncio
from aiohttp import ClientSession
from Util import *

URL = "http://localhost:8000/info"
REQUEST_LIMIT = 100

async def run():
    async with ClientSession() as session:
        async with session.get(URL) as response:
            response = await response.read()
            print("Response :: ", response)

async def callInfoAPI():

    taskList = []

    for each in range(0,REQUEST_LIMIT):
        task = asyncio.create_task(run())
        taskList.append(task)

    await asyncio.wait(taskList)

loop = asyncio.get_event_loop()

loop.run_until_complete(callInfoAPI())