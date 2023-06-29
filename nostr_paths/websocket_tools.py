import websockets
from pynostr.event import Event
import json
import asyncio

async def send_data(data: str, relay: str) -> str:
    async with websockets.connect(relay) as websocket:
        await websocket.send(data)
        return await websocket.recv()

async def publish_event(event: Event, relay: str) -> str:
    return await send_data(f'{event}', relay)


async def get_note(relay_query: str, relay: str) -> json:
    json.loads(f'{asyncio.run(send_data(relay_query, relay))}')[2:]
