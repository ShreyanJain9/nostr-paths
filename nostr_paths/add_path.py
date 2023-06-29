from pynostr.event import Event
def add_path(event: Event, path: str) -> Event:
    event.tags.append(["u", path])
    return event
