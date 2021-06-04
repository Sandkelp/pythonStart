import json
from secrets import spotify_user_id
import requests


class CreatePlaylist:
    
    
    def __init__(self):
        self.user_id = spotify_user_id
    #log on to youtube
    def get_youtube_client(self):
        pass
        #get liked videos
    def get_liked_videos(self):
        pass

    #create a playlist
    def create_play_list(self):
        request_body = json.dumps({

        
        "name": "Automated Playlist",
        "description": "I did not make this",
        "public":false
        })
        query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data = request_body,
            headers ={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format()            }
        )
        reponse_json = response.json()

        #playlist id
        return response_json["id"]

    #search for a song
    def get_spotify_uri(self, song_name, artist):
        query 


    #add song to playlist
    def add_song_to_playlist(self):
        pass


    