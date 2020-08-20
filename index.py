import praw
from instabot import Bot 
import os
import shutil
from dotenv import load_dotenv
import requests
load_dotenv()


#Setting up Reddit Client
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
reddit = praw.Reddit(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    user_agent="my user agent")


# Setting up Instagram Client
user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
bot = Bot() 
bot.login(username = user_name,  
          password = password) 


#Initializing variables
sub_list = ["NatureIsFuckingLit", "EarthPorn"]
posts = []
limit = 7
path = f"{os.getcwd()}/images"


#Removing old images folder first so that we do not upload previous images again later.
if os.path.isdir(path):
    print("Yes path exists. Deleting.")
    shutil.rmtree(path)
print("Creating new directory.")
os.makedirs(path)
print("Created new directory.")


#Getting posts from Reddit
print("Downloading pictures.")
for sub in sub_list:
    for post in reddit.subreddit(sub).hot(limit=limit):
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
                "url": post.url,
                "source": sub
            }
            posts.append(item)


#Uploading pictures to Instagram
print("Uploading Pictures")
for post in posts:
    bot.upload_photo(f"images/{post['id']}.jpg", 
                 caption =f"{post['title']} by @{post['author']} on r/{post['source']}.") 

