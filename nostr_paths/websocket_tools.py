import websockets

async def send_data(data: str, relay: str) -> str:
    async with websockets.connect(relay) as websocket:
        await websocket.send(data)
        return await websocket.recv()
