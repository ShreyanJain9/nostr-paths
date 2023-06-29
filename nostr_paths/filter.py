from pynostr.filters import Filters
from pynostr.key import PublicKey
import urllib.parse
import random

def uri_to_request(uri: str) -> str:
    # Extracting the path from the URL string
    path = urllib.parse.urlparse(uri).path
    # Extracting the public key from the path
    npub = uri.split("/")[2]
    publickey = PublicKey('').from_npub(npub).hex()
    filterlist = Filters(authors=[f"{publickey}"])
    filterlist.add_arbitrary_tag("u", [path])
    random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(64))
    relay_query = f'["REQ", "{random_string}", {filterlist}]'
    return relay_query
