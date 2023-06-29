import websockets

async def send_data(event, relay):

    async with websockets.connect(relay) as websocket:
        message = f'{event}'
        await websocket.send(message)
        return await websocket.recv()
