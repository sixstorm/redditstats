# Check every 5 minutes up to 1 hour?
# Or check the activity of the last hour?
# Function: Writing to SQL DB
# Function: After 1 hour, remove duplicates
# Function: Get latest from Reddit
# Test edit 2

import praw
import datetime
import requests
import sqlite3
import datetime
import time
from pprint import pprint


db = sqlite3.connect('test.db')
r = praw.Reddit(user_agent="/r/teamtuck Stats Test")
subreddit = r.get_subreddit("todayilearned")
cur = db.cursor()
reddict = {}


def addtosqldb(title, score, dtp):
	cur.execute('''INSERT INTO Reddit (Title,Score,DTP) VALUES(?,?,?)''', (title,score,dtp))

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

def removesqldup():
	print "Attempting to remove all duplicates in SQL DB"
	cur.execute('''DELETE FROM Reddit WHERE rowid NOT IN (SELECT MIN(rowid) FROM Reddit GROUP BY Title,DTP)''')

def getrowcount():
	print "Attempting to get count of Reddit posts"
	for row in cur.execute('''SELECT COUNT(Title) FROM Reddit'''):
		rowcount = row[0]
	print "There are %s posts in your DB!" % rowcount

def gettime():
	timenow = time.strftime("%Y-%m-%d %H:%M:%S")

def showlasthour():
	timenow = datetime.datetime.now()
	starttime = timenow.replace(minute=0, second=0, microsecond=0)
	cur.execute('''SELECT * FROM Reddit WHERE (DTP) >= (?)'''), starttime
	rows = cur.fetchall()
	for row in rows:
		print row

def addtodictionary():
	cur.execute('''SELECT * FROM Reddit''')
	rows = cur.fetchall()
	#for row in rows:


for submission in subreddit.get_new(limit=100):
	# Convert UTC to Readable Timestamp
	convertedts = datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')

	# Create Table
	#print "Creating Table"
	#createnewsqltable()

	title = submission.title
	score = submission.score

	# Add to SQL DB
	addtosqldb(submission.title, submission.score, convertedts)


'''
	# Print all rows in DB with pprint
	cur.execute("SELECT * FROM Reddit")
	rows = cur.fetchall()
	for row in rows:
		pprint(row)
'''

# Delete duplicates in SQL DB
removesqldup()

# Get row count
getrowcount()

# Commit to DB
print "Committing to DB"
db.commit()

# Dictionary Test


#print "Test print"
#showlasthour()
