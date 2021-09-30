import asyncio
import datetime
import random
import websockets

def dealCard():
    cards = ['J', '9', 'A', '10', 'K', 'Q', '8', '7']

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

async def main():
    async with websockets.serve(time, "localhost", 5678):
        await asyncio.Future()  # run forever

asyncio.run(main())