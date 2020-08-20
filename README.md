# RedGram
A python script that fetches posts from Reddit to post on Instagram.

---

## Table of contents
* [General info](#general-info)
* [Screenshot](#screenshot)
* [Requirements](#Requirements)
* [Getting Started](#Getting-Started)
* [Contact](#Contact)

---

## General info

I came across a medium post where someone used python to post picture on Instagram from posts in Reddit. Before I could read it, I lost the link. So I decided to create my own python script that would extract images from subreddits in Reddit and post in on one of my Instagram account.

---

## Screenshot
![In Action](https://imgur.com/qdzKPTL.gif)

---

## Requirements
- Reddit - Go [here](https://www.reddit.com/prefs/apps) and create a reddit app which will give you the reddit client id and secret
- Instagram - Your Username and Password.

---

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Get into the folder using `cd RedGram`.
3. Install the requirements using `pip install -r requirements.txt`.
    * Make sure you use Python 3.
    * You may want to use a virtual environment for this.
4. Create a .env file and fill it with these four informaion
    - `CLIENT_ID=your_reddit_client_id_without_quotes`
    - `CLIENT_SECRET=your_reddit_client_secret_without_quotes`
    - `USER_NAME=your_instagram_username_without_quotes`
    - `PASSWORD=your_instagram_password_without_quotes`
5. Inside the index.py you can put your preference of subreddits in the "sub_list" variable and also you can control how many posts PRAW will extract by changing the value of the variable "limit".
6. Run the index.py in terminal.
 
---

## Contact
  * [@41x3n](https://twitter.com/41x3n) - feel free to contact me!
