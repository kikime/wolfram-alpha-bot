import os

import praw
import wolframalpha

WA_APP        = os.environ["wolframalpha_app_id"]
CLIENT_ID     = os.environ["reddit_client_id"]
CLIENT_SECRET = os.environ["reddit_client_secret"]
USERNAME      = os.environ["reddit_username"]
PASSWORD      = os.environ["reddit_password"]

def main():
    r = praw.Reddit(
        user_agent    = "wolfram-alpha-bot 007 (by /u/SteveCCL)",
        client_id     = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        username      = USERNAME,
        password      = PASSWORD
)

if __name__ == "__main__":
    main()
