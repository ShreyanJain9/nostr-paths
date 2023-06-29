import asyncio
from pynostr.event import Event
from pynostr.key import PrivateKey
from nostr_paths.add_path import add_path

private_key = PrivateKey()
public_key = private_key.public_key

event = Event(input("Enter the content of your note here: "))
path = input("Enter the path of your note here (with a leading / ): ")
add_path(event, path)
event.sign(private_key.hex())

relay = "wss://relay.damus.io"



asyncio.get_event_loop().run_until_complete(send_data(event, relay))

nostr_uri = f"nostr://{public_key.bech32()}{path}"

print(f"\n{nostr_uri}\n")

