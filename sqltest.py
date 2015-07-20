import praw
import datetime
import requests
import sqlite3
import datetime

db = sqlite3.connect('test2.db')
cur = db.cursor()
#print "Creating DB in test2.db"
#cur.execute('''CREATE TABLE Reddit(Title TEXT, Score INT, DTP TEXT)''')

title = "Test Title"
score = "1"
dtp = "5162015"

print "Inserting data . . . "
try:
	cur.execute('''INSERT INTO Reddit(Title,Score,DTP) VALUES(?,?,?)''', (title,score,dtp))
except:
	print "Failure inserting data"
	exit()
	

db.commit()
