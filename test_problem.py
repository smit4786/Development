import requests
import random

def search_songs(artist_name, num_songs=10):
    base_url = 'https://itunes.apple.com/search'

    params = {
        'term': artist_name,
        'media': 'music',
        'entity': 'musicTrack',
        'limit': num_songs,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if 'results' in data:
            songs = data['results']

            # Shuffle the list of songs
            random.shuffle(songs)

            for i, song in enumerate(songs, 1):
                print(f"{i}. {song['trackName']} by {song['artistName']}")

        else:
            print(f"No songs found for {artist_name}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

if __name__ == "__main__":
    artist_name = input("Enter artist name: ")
    search_songs(artist_name)
