# Check every 5 minutes up to 1 hour?
# Or check the activity of the last hour?
# Function: Writing to SQL DB
# Function: After 1 hour, remove duplicates
# Function: Get latest from Reddit

import praw
import datetime
import requests
import sqlite3
import datetime
from pprint import pprint

uniqueid = 1
db = sqlite3.connect('test.db')
r = praw.Reddit(user_agent="/r/teamtuck Stats Test")
subreddit = r.get_subreddit("todayilearned")
cur = db.cursor()


def addtosqldb(title, score, dtp):

	
	print "Adding post into SQL DB"
	cur.execute('''INSERT INTO Reddit (Title,Score,DTP) VALUES(?,?,?,?)''', (title,score,dtp,uniqueid))
	uniqueid += 1
	print uniqueid

def createnewsqltable():
	# Create table "Reddit"
	print "Creating DB in Test.db"
	cur.execute("CREATE TABLE Reddit(Title TEXT, Score INT, DTP TEXT, ID INT)")

def deletesqltable():
	# Drop the table
	try:
		cur = con.cursor()
		cur.execute("DROP TABLE Test")
		cur.commit()
	except:
		print "Cannot drop table"
		exit()

for submission in subreddit.get_new(limit=10):
	# Convert UTC to Readable Timestamp
	convertedts = datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')

	#print "-"*20
	#print "Converted time: %s" % convertedts

	# Create Table
	#print "Creating Table"
	#createnewsqltable()

	title = submission.title
	score = submission.score

	# Add to SQL DB
	print "Adding data to SQL DB"
	addtosqldb(submission.title, submission.score, convertedts)

	# Print all rows in DB with pprint
	cur.execute("SELECT * FROM Reddit")
	rows = cur.fetchall()
	for row in rows:
		pprint(row)

db.commit()
