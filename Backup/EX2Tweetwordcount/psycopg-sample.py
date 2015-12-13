#Sample code snippets for working with psycopg


#Connecting to a database
#Note: If the database does not exist, then this command will create the database

import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
#cur.execute('''CREATE TABLE Tweetwordcount
#       (word TEXT PRIMARY KEY     NOT NULL,
#       count INT     NOT NULL);''')
#conn.commit()
#conn.close()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

cur = conn.cursor()


Count = 3
Word = 'bat'
insert_word = 1

cur.execute("SELECT word, count from Tweetwordcount")
check = cur.fetchall()
for c in check:
  if c[0] == Word:
    cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (c[1] + Count, Word))
    conn.commit()
    insert_word = 0
  else:
    pass
   
if insert_word == 1:
  cur.execute("INSERT INTO Tweetwordcount (word,count) \
              VALUES (%s, %s)", (Word, Count));
  conn.commit()

#uCount = 7
#uWord = 'cat'

#Update
#Assuming you are passing the tuple (uWord, uCount) as an argument
#cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (uCount, uWord))
#conn.commit()

#Select
cur.execute("SELECT word, count from Tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
