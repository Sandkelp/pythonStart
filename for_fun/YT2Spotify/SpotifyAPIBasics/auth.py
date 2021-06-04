client_id = '1805d978e72b4d11820d6dfc1dd19823'
client_secrect = '89b64947df0840a2817ae4dd208ab1c8'

token_url = "https://accounts.spotify.com/api/token" #token url
method = "POST" #defines the method
token_data = {
    "grant_type": "client_credentials" #gives the token data
}

import base64 #imports the base 64 lib
import datetime #imports datetime
def get_token():
    client_creds = f"{client_id}:{client_secrect}" 
    client_creds_b64 = base64.b64encode(client_creds.encode()) # takes the client creds encodes it into bytes then encodes it into base 64
    token_header = {
        "Authorization": f"Basic {client_creds.decode()}" #decodes it back so that it can be passed back through
    }

    response = requests.post( #gets the token
        token_url, 
        data=token_data, 
        headers=token_data
        )

    response_json = response.json() #gets the json file
    valid_request = response_json.status_code in range(200,299) #boolean to see if code was recived

    spotify_token = response_json['access_token']#gets the access token from the json api response
    if valid_request:
        now = datetime.datetime.now() #gets the time rn
        expires_in = response_json['expires_in'] #gets the how long it expires in 
        expires = now + datetime.timedelta(seconds=expires_in) # gets the time that it expires
        did_expire = expires < now #boolen that says if it expired
    return spotify_token

class SpotifyAPI(object):
    spotify_token = None
    expires = None
    client_id = None
    client_secrect = None

    def __init__(self, spotify_token, expires, client_id, client_secrect, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secrect = client_secrect

    def get_token_header(self):
        pass

    def get_token_data(self):
        return {
            "grant_type": "client_credentials" #gives the token data
        }


    def extract_access_token(self):
        return

    
