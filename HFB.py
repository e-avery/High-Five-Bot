# High_Five_Bot v1.0.0
# Written in PRAW (Python Reddit API Wrapper)
# Python v3.6

import os
import time
import praw
from datetime import datetime
from random import randint

# Create instance, identifying user agent
reddit = praw.Reddit(client_id='',
		     client_secret='',
		     password='',
		     user_agent='',
		     username='')

# Feedback on login status
if reddit.user.me() == "High_Five_Bot":
	print("I am High_Five_Bot. Logged in and ready to go.")

# set up for r/bottesting--change to r/all after completion
subreddit = reddit.subreddit('all')

# Array of high five GIFs
hf_gifs = ["https://i.imgur.com/NAkvu0L.gifv", "https://i.imgur.com/TITkVpi.gifv", "https://i.imgur.com/SsZJSyy.gifv", "https://i.imgur.com/W3LGywp.gifv", 
"https://i.imgur.com/TX2oxf3.gifv", "https://i.imgur.com/JpDHdLd.gifv", "https://i.imgur.com/lGpQ0ak.gifv",
 "https://i.imgur.com/P70igZx.gifv", "https://i.imgur.com/XiDPAlW.gifv", "https://i.imgur.com/PXA8cVT.gifv"]

# String attachment for ID
botstat = ("""
*****
^("I am a good bot. When I'm called with )!high-five^( or )!highfive,^( I return a sweet high-five GIF. Call me up if you ever need to high-five someone.")
""")

# Check to see if already responded
def resp_check(var):
	with open(os.environ['USERPROFILE']+'/Documents/GitHub/HFBot/IDs.txt') as nfile:
		for lines in nfile.readlines():
			if str(var) in lines:
				return 1
			else:
				f = 0
	return f

def crawl():
	print("Searching...")
	for comment in subreddit.stream.comments():
		if ((comment.body.lower() == "!highfive") or (comment.body.lower() == "!high-five")) and (comment.author.name != 'High_Five_Bot') and (resp_check(comment) == 0):
			# reply to parent comment where the second argument is the UL for the array index
			reply = "%s high-fived %s" % (comment.author, comment.parent().author)
			comment.reply("[" + reply + "](" + hf_gifs[randint(0,2)] + ")" + botstat)
			with open(os.environ['USERPROFILE']+'/Documents/GitHub/HFBot/IDs.txt', 'a') as file:
				file.write(str(comment) + "\n")
			print("Found a call.")
			

while True:
	try:
		print("Starting my main method.")
		crawl()
	except Exception as e:
		with open(os.environ['USERPROFILE']+'/Documents/GitHub/HFBot/BotErrors.txt', 'a') as file:
			file.write(str(datetime.now()) + " - " + str(e) + "\n")
		print("Meh, got an error.")
		continue
	except praw.exceptions.APIException as e:
		print(e)
		if e.error_type == "RATELIMIT":
			print("Haven't quit, just sleeping on the job.")
		# Remove this part once Karma is built up and rate limit is gone/diminished
		time.sleep(600)
		continue
