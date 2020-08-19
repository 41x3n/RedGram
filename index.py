import praw
import os
import shutil
from dotenv import load_dotenv
import requests

#Setting up Reddit Client
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
reddit = praw.Reddit(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    user_agent="my user agent")

#Initializing variables
sub_list = ["NatureIsFuckingLit", "EarthPorn"]
posts = []
path = f"{os.getcwd()}/images"

#Removing old images folder first so that we do not upload previous images again later.
if os.path.isdir(path):
    print("Yes path exists. Deleting")
    shutil.rmtree(path)
os.makedirs(path)

#Getting posts from Reddit
for sub in sub_list:
    for post in reddit.subreddit(sub).hot(limit=5):
        if ".jpg" in post.url and "imgur" not in post.url:
            #Downloading files
            response = requests.get(post.url)
            file = open(f"images/{post.id}.jpg", "wb")
            file.write(response.content)
            file.close()
            item = {
                "id": post.id,
                "author": post.author,
                "title": post.title,
                "url": post.url
            }
            posts.append(item)


