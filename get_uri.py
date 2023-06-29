from nostr_paths.filter import uri_to_request
from nostr_paths.websocket_tools import send_data
import asyncio
relay_query = uri_to_request(input("Enter the nostr:// uri of the event you want: "))

print(asyncio.run(send_data(f'{relay_query}', 'wss://relay.damus.io')))
