import json
import requests



class CreatePlaylist:
    def __init__(self):
        self.user_id = "kqqwqlg2ll1p2gjnlguf8w2m6"
        self.spot_token = "BQADtBIwhoPf5iQvICzfmLr8hT7HlyiiF2grLlzQzy7M7TRrW-SwuW1QdTTZTMGKv0sxW7aJPsFN7osXDLjTtDNfjwf-3q6nSMINWZBcK1WFGwe4X3XXwcARMod7HTMEGsETMZ_mD5ABkgMSnVcbWVlXK2u0Fy_zIjWWkZScG4k16l-KVAPR35aoEwD7n8lzviOcZFQYIpWPriLUL03fm0Gb5KWa5yA8Lvz_lunglyR595zuQqxChKtse5VcYzZl"
    def get_youtube_client(self):
        pass
    def get_liked_videos(self):
        pass
    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query, 
            data=request_body,
            headers={
                "Content-Type": "appliction/json"
                "Authorization":"Bearer {}".format(self.spot_token)
            }
        )
        response_json = response.json()
        return response_json["id"]
        
    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type":"appliction/json"
                "Authorization": "Bearer {}".format(self.spot_token)
            }
        )
        response_json =  response.json()
        songs = response_json["tracks"]["items"]
        
        uri = [0]["uri"]
        return uri
        

    def add_song_to_playlist(self):
        pass
