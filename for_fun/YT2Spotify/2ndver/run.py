from youtube_client import YouTubeClient
from spotify_client import SpotifyClient
import os

def run():
    youtube_client = YouTubeClient('C:\\Users\\ssubh\Downloads\\client_secret_1019903256326-0us041ebas5b9f759ao2fr7uqhd8cn5l.apps.googleusercontent.com.json')
    spotify_client = SpotifyClient('BQCLb58BY7i2EaDwi4FRYjN5CDbV6okQBwhJkSZICEEZQx5nMYUaPd0CyHReIzCkuOSvcePZDN2YgQuWaslaPjh6s_F20AMJJQi1UNjexk3NPBpvTHc6gVicGOFx-qQ3wYJvle68D-XzXBhv8wBFKIoWMBWCWolIdKhX6tvqwFePkuYaEfklgE6_U9Y7UydoRmA3Pmcx2pSaPnGnXPDsLq0W_oWQJ_2A66HPcWRf1l2ruMsC0vnuLBIN_RJBA_H5')
    playlists = youtube_client.get_playlists()
    

    for index, playlist in enumerate(playlists):
        print(f"{index}:{playlist.title}")
        choice = int(input("Enter your choice: "))
        chosen_playlist = playlists[choice]

        print(f"You selected: {chosen_playlist.title}")

        songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
        print(f"attempting to add {len(songs)}")

        for song in songs:
            spotify_song_id = spotify_client.search_song(song.artist, song.track)
            if spotify_song_id:
                added_song = spotify_client.add_song_to_spotify(spotify_song_id)
                if added_song:
                    print(f"Added {song.artist}")
    

if __name__ == '__main__':
    run()