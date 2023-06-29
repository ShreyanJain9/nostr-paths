import asyncio
import websockets

class RelayList:
    def __init__(self, *args):
        self.relays = [*args]

    async def send_data(self, event, relay):
        async with websockets.connect(relay) as websocket:
            message = f'{event}'
            await websocket.send(message)
            return await websocket.recv()

    async def publish(self, event):
        tasks = []
        for relay in self.relays:
            task = asyncio.create_task(self.send_data(event, relay))
            tasks.append(task)
        await asyncio.gather(*tasks)
