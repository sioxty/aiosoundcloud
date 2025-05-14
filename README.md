# AIOSoundCloud

## Installation

To install the library, use `pip`:

```bash
pip install https://github.com/sioxty/aiosoundcloud
```

## Usage Example
### SoundCloudClient
```python
import asyncio
from aiosoundcloud import SoundCloudClient

async def main():
    client = SoundCloudClient(client_id="YOUR_CLIENT_ID")
    
    # Searching for tracks
    search_results = await client.search(query="lofi hip hop", limit=5)
    print("Результати пошуку:")
    for track in search_results.get("collection", []):
        print(f"Назва: {track['title']}, Автор: {track['user']['username']}")
    
    
    # Fetching track details by ID
    track_id = search_results["collection"][0]["id"]
    track_details = await client.get_track(_id=track_id)
    print(f"Назва треку: {track_details['title']}, Прослуховування: {track_details['playback_count']}")

asyncio.run(main())
```
### SoundCloud
```python
import asyncio
from aiosoundcloud import SoundCloudClient

async def main():
    client = SoundCloudClient(client_id="YOUR_CLIENT_ID")
    
    search_results = await client.search(query="lofi hip hop", limit=5)
    print("Result search:")
    for track in search_results.get("collection", []):
        print(f"Title: {track['title']}, Author {track['user']['username']}")
    
    
    track_id = search_results["collection"][0]["id"]
    track_details = await client.get_track(_id=track_id)
    print(f"Title track: {track_details['title']}, {track_details['playback_count']}")

asyncio.run(main())
```
### How get clinent_id
```python
import asyncio
from aiosoundcloud import get_client_id

async def main():
    client_id = await get_client_id()
    print(f"Your client_id: {client_id}")

asyncio.run(main())
```
### How to Get a Link

```python
import asyncio
from aiosoundcloud import SoundCloud

async def main():
    client = SoundCloud(client_id="YOUR_CLIENT_ID")
    
    
    tracks = await client.search(query="lofi hip hop", limit=1)
    track = tracks[0]
    
    # Get the stream URL for the track
    stream_url = await client.get_stream_url(track=track)
    print(f"Посилання на стрім: {stream_url}")

asyncio.run(main())
``` 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
