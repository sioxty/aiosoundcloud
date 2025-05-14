# AIOSoundCloud

## Installation

Install the library using `pip`:

```bash
pip install git+https://github.com/sioxty/aiosoundcloud.git
```

## Usage Example

### `SoundCloudClient` – Basic API Access

```python
import asyncio
from aiosoundcloud import SoundCloudClient

async def main():
    client = SoundCloudClient(client_id="YOUR_CLIENT_ID")
    
    # Search for tracks
    search_results = await client.search(query="lofi hip hop", limit=5)
    print("Search results:")
    for track in search_results.get("collection", []):
        print(f"Title: {track['title']}, Author: {track['user']['username']}")
    
    # Fetch track details by ID
    track_id = search_results["collection"][0]["id"]
    track_details = await client.get_track(_id=track_id)
    print(f"Track title: {track_details['title']}, Plays: {track_details['playback_count']}")

asyncio.run(main())
```

### `SoundCloud` – High-Level Access (e.g., Stream URLs)

```python
import asyncio
from aiosoundcloud import SoundCloud

async def main():
    client = SoundCloud(client_id="YOUR_CLIENT_ID")
    
    # Search for a track
    tracks = await client.search(query="lofi hip hop", limit=1)
    track = tracks[0]
    
    # Get streamable URL
    stream_url = await client.get_stream_url(track=track)
    print(f"Stream URL: {stream_url}")

asyncio.run(main())
```

### How to Get a `client_id`

```python
import asyncio
from aiosoundcloud import get_client_id

async def main():
    client_id = await get_client_id()
    print(f"Your client_id: {client_id}")

asyncio.run(main())
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
