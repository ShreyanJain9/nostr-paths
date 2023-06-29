from nostr_paths.filter import uri_to_request
from nostr_paths.websocket_tools import send_data
import asyncio
import json
relay_query = uri_to_request(input("Enter the nostr:// uri of the event you want: "))

print(json.loads(f'{asyncio.run(send_data(f"{relay_query}", "wss://relay.damus.io"))}')[2])

## I will clean up that ugly mess, I promise
