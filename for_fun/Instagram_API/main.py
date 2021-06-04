from instagram_private_api import Client, ClientCompatPatch
import secrets
import yaml
import json
user_name = secrets.user_name
password = secrets.password

api = Client(user_name, password)
user_id = api.authenticated_user_id
rank_token = api.generate_uuid()

user_followers = str(api.user_followers(user_id, rank_token))

user_followers_json = json.dumps(yaml.safe_load(user_followers),indent=4)

user_followers_json2 = json.loads(user_followers_json)


user_following = str(api.user_following(user_id, rank_token))
user_following_json = json.dumps(yaml.safe_load(user_following),indent=4)
user_following_json2 = json.loads(user_following_json)




followers = []
for follower in user_followers_json2["users"]:
    followers.append(follower["username"])

following = []
for user in user_following_json2["users"]:
    following.append(user["username"])

for user in following:
    if user not in followers:
        print(user)


    




