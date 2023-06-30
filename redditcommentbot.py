import praw
import random
import time

reddit = praw.Reddit(
    client_id="-your client id goes here-",
    client_secret="-your client secret goes here-",
    user_agent="-name your bot something-", #<console:-botname-:-botversion-> for scripts for example
    username="-your reddit account goes here-",
    password="-reddit account's password-")

subreddit = reddit.subreddit("-subreddit of your choice-")

list_to_store_replies = ["-reply1-", 
            "-reply2-",
            "-reply3-",
            "-reply4-",
            "-reply5-"]

for submission in subreddit.hot(limit=100): #TODO: set rate limit as you want, try not to spam much
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "-keyword to target-" in comment_lower:
                random_index = random.randint(0, len(list_to_store_replies) - 1)
                comment.reply(list_to_store_replies[random_index])
                time.sleep(60) #TODO: increase it if you do not want to spam comments
