# Nostr Paths: Just Thoughts, Not a NIP Yet

## Event Structure
An event would follow the following structure:
```json
{
  "id": <event_id>,
  "pubkey": <event_creator_pubkey>,
  "created_at": <timestamp>,
  "kind": <event_kind>,
  "tags": ["....", ["u", <event_path>]],
  "content": <event_content>,
  "sig": <event_signature>,
}
```

Each event consists of the following attributes:
- **id**: the unique identifier of the event.
- **pubkey**: the public key of the event creator.
- **created_at**: the timestamp indicating when the event was created.
- **kind**: the type or category of the event.
- **tags**: an array of tags associated with the event.
	- **u**: a tag for the path associated with the event. (“u“ for uri, since “p” already means pubkey.)
- **content**: the content or payload of the event.
- **sig**: the signature of the event.

## Querying the Relay
To retrieve events from the relay using their path, you can use the following query format:
```json
["REQ", <subscription_id>, {“#u”: [<event_path>], “authors”: [<event_creator_pubkey>]}]
```
By specifying the **path** and **pubkey** in the query, you can request the relay to provide relevant events. The relay will return all events that match the given path and belong to the specified pubkey.

Nothing new has to be implemented for that, because it’s all in NIP-01 itself!
## But why?
By giving Nostr events paths, we get:
- Simplified Version History: Nostr Paths serve as a version history, allowing users to track the evolution of an event over time.
- Directory Listing: Nostr Paths also function as a directory listing, providing a convenient way to organize events based on their paths. (This one’s a bit iffy, as tag queries don’t support wildcards. It might require having a separate “directory” tag of some sort?)

## As a URI
To interact with the relays using Nostr Paths, clients can convert a path like `nostr:npubsomething/some/event` into a request to the relays:

```json
["REQ", “<subscription_id>”, {”#u": ["/some/event/"], "authors": ["<hex version of npubsomething>”]}]
```

(should it be something other than nostr:// since that uri scheme is already designed to use noteids?)

## Demo

This repository contains a minimal working Python-based demonstration of two things: creating an event with the "u" tag and retrieving it from a relay based on its theoretical nostr:// URI.

To try it out, install all the requirements using pip, and then run
```sh
python3 publish.py
```
and enter the note content and then the path you want it at. The script will use a randomly-generated keypair for now, and returns a URI like:
`nostr://npub1lhmf0kpdcfa0p8vfcwhwkjfyp8dawkkesh7c8qj7cwfw083wj4asje928h/hello/world`

To view your event, you can then take the URI and run
```sh
python3 get_uri.py
```
and enter the nostr:// uri. It will then return the JSON contents of your note!
