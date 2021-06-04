#1. Log into YouTube
#2. Get the Liked Videos
#3. Create a new playlist
#4. Find the song
#5. Add song to playlist
from secrets import spotify_user_id, spotify_token
import json
import requests
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

class CreatePlaylist:
    def __init__(self):
        self.userID = spotify_user_id
        self.spotifyToken = spotify_token
        self.youtubeClient = self.get_yt_client()

    def get_yt_client(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "C:\\Users\\ssubh\Downloads\\client_secret_1019903256326-0us041ebas5b9f759ao2fr7uqhd8cn5l.apps.googleusercontent.com.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

    def get_likes(self):
        request = self.youtube_client.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()

        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])
            video = youtube_dl.YouTubeDL({}).extract_info(youtube_url, download=False)

            song_name = video["track"]
            artist = video["artist"]
            
            self.all_song_info[video_title]={
                "youtube_url": youtube_url,
                "song_name": song_name,
                "artist": artist, 
                "spotify_uri":self.get_spotify_uri(song_name, artist)
            }

    def create_playlist(self):
        requestBody = json.dumps({
            "name": "Youtube playlist",
            "description": "This playlist was imported from youtube",
            "public":True
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.userID)

        response = requests.post(
            query,
            data=requestBody,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(self.spotifyToken)
            }
        )

        response_json = response.json()
        return response_json["id"]

    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name, 
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(self.spotifyToken)
            }
        )

        response_json = response.json()
        return response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]



    def add_song_to_playlist(self):
        self.get_likes()

        uris = []
        for song in self.all_song_info.items():
            uris.append(info["spotify_uri"])
        
        playlist_id = self.create_playlist()

        request_data = json.dumps(uris)
        
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

        response = requests.post(
            query,
            data = request_data,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(self.spotifyToken)
            }
        )

        response_json = response.json()
        return response_json

if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()