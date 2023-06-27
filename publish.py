import asyncio
import websockets
from pynostr.event import Event
from pynostr.key import PrivateKey

private_key = PrivateKey()
public_key = private_key.public_key

print(f"Hex Private key: {private_key}")
print(f"Hex Public key: {public_key}")

event = Event(input("Enter the content of your note here: "))
path = input("Enter the path of your note here (with a leading / ): ")
event.tags = [["u", path]]

event.sign(private_key.hex())

print("\nEvent: \n")
print(event)
print("\n")

relay = input("Enter the relay (only one) to publish to here, beginning with the wss:// prefix: ")

async def send_data(event, relay):

    async with websockets.connect(relay) as websocket:
        message = f'{event}'
        await websocket.send(message)
        response = await websocket.recv()
        print("\nReceived message from relay:", response)

asyncio.get_event_loop().run_until_complete(send_data(event, relay))

nostr_uri = f"nostr://{public_key.bech32()}{path}"

print(f"\nThe theoretical nostr URI for that event would be: {nostr_uri}\n")

relay_query = f'["REQ", "randomstringijustmadeupihr84hrf43", {{"#u": ["{path}"], "authors": ["{f"{public_key}"[0:7]}"]}}]'

print(f'The request you would send to a relay to find your note is: {relay_query}\n')


