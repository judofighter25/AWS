
import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")


if len(sys.argv) < 3:
  print "Input error.  Missing arguements?"
else:
  arg1 = sys.argv[1]
  arg2 = sys.argv[2]

cur = conn.cursor()

cur.execute("SELECT word, count from Tweetwordcount WHERE count BETWEEN %s AND %s", (arg1, arg2))
records = cur.fetchall()
conn.commit()
for rec in records:
  print "word = ", rec[0]
  print "count = ", rec[1], "\n"

