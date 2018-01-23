# High_Five_Bot
# Written in PRAW (Python Reddit API Wrapper)
# Python v3.6

import praw
import time
from datetime import datetime
from random import randint

# Create instance, identifying user agent
reddit = praw.Reddit(client_id='',
		     client_secret='',
	             password='',
		     user_agent='High-Five Bot v0.1, by u/WadeEffingWilson',
		     username='High_Five_Bot')

# Feedback on login status
if reddit.user.me() == "High_Five_Bot":
	print("Logged in and ready to go.")

# set up for r/bottesting--change to r/all after completion
subreddit = reddit.subreddit('bottesting')

# Array of high five GIFs
hf_gifs = ["https://i.imgur.com/NAkvu0L.gifv", "https://i.imgur.com/TITkVpi.gifv", "https://i.imgur.com/SsZJSyy.gifv"]

# String attachment for ID
botstat = ("*****"
"I am a bot. When I'm called with !high-five or !highfive, I return a sweet high-five GIF. Call me up if you ever need to high-five someone.")

# Error catch variable for troubleshooting
errors = []

def crawl():
	for comment in subreddit.stream.comments():
		if (comment.body.lower() == "!highfive") or (comment.body.lower() == "!high-five") and (comment.author.name != 'High_Five_Bot'):
			# reply to parent comment where the second argument is the UL for the array index
			reply = "%s high-fived %s" % (comment.author, comment.parent().author)
			comment.reply("[" + reply + "](" + hf_gifs[randint(0,2)] + ")" + botstat)
			
# Add conditional __main__ statement before here
while True:
	try:
		print("Starting...")
		crawl()
	except Exception as e:
		print("There was an issue.")
		time.sleep(5)
		continue
