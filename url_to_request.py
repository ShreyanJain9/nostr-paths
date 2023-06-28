import websockets
import asyncio
from nostr_paths.filter import uri_to_request

relay_query = uri_to_request(input("Enter the nostr:// uri of the event you want: "))

print(f'The request you would send to a relay to find your note is: {relay_query}\n')


async def send_relay_query(relay_query: str):
    # WebSocket server URL
    websocket_url = "wss://relay.damus.io"

    try:
        async with websockets.connect(websocket_url) as websocket:
            # Send the relay query
            await websocket.send(relay_query)
            print("Relay query sent successfully.")

            # Receive and process the server's response
            response = await websocket.recv()
            print("Server response:", response)

    except websockets.exceptions.ConnectionClosedError:
        print("WebSocket connection closed unexpectedly.")

asyncio.run(send_relay_query(f'{relay_query}'))
