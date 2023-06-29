from pynostr.event import Event
from pynostr.key import PrivateKey
from copy import copy
class KeyPair:

    def __init__(self, hex_private_key: str):
        self.private_key = PrivateKey.from_hex(hex_private_key)
        self.public_key = self.private_key.public_key
        self.npub = self.public_key.npub
        self.nsec = self.public_key.nsec

    def sign(self, event: Event) -> Event:
       event.sign(self.private_key)
       return event

