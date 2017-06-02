import os
import re
import time

import praw
import wolframalpha

WA_APP        = os.environ["wolframalpha_app_id"]
CLIENT_ID     = os.environ["reddit_client_id"]
CLIENT_SECRET = os.environ["reddit_client_secret"]
USERNAME      = os.environ["reddit_username"]
PASSWORD      = os.environ["reddit_password"]

IS_RELEVANT = re.compile(r"\s*\+?/?u/wolfram-alpha-bot\s+")

def main():
    r = praw.Reddit(
        user_agent    = "wolfram-alpha-bot 007 (by /u/SteveCCL)",
        client_id     = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        username      = USERNAME,
        password      = PASSWORD
    )
    wa = wolframalpha.Client(WA_APP)

    print("Bot up and running")

    while 1:
        for message in r.inbox.unread():
            try:
                if re.match(IS_RELEVANT, message.body):
                    print(message.body)
                message.mark_read()
            except Exception as e:
                print("An error occured. ({})".format(str(e)))
                print("Retrying in a minute.")
                time.sleep(60)


if __name__ == "__main__":
    main()
