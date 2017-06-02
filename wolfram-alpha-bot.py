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

IS_RELEVANT = re.compile(r"\s*\+?/?u/wolfram-alpha-bot\s+(.*)$", re.IGNORECASE)

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
                match = re.match(IS_RELEVANT, message.body)
                if match:
                    res = wa.query(match.group(1))
                    if res["@success"] == "true":
                        message.reply(match.group(1) + " = " + next(res.results).text + "\n\n^Beep ^blop ^I'm ^a ^bot. ^Message ^SteveCCL ^if ^there's ^anything ^wrong ^with ^me.")
                    else:
                        message.reply("Wolfram|Alpha does not know how to interpret your input.\n\n^Beep ^blop ^I'm ^a ^bot. ^Message ^SteveCCL ^if ^there's ^anything ^wrong ^with ^me.")

                message.mark_read()
            except Exception as e:
                if 'RATELIMIT: ' in str(e):
                    t = int(str(e).split(' ')[10])
                    print("RATELIMIT exceeded. Sleeping for {} minutes....".format(t))
                    time.sleep(60 * t)
                else:
                    print("An error occured. ({})".format(str(e)))
                    print("Retrying in a minute.")
                    time.sleep(60)


if __name__ == "__main__":
    main()
