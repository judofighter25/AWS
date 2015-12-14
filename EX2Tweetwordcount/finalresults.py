
import sys

#input = raw_input('Enter a word: ')
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")


if len(sys.argv) == 1:
  arg1 = "All"
else:
  arg1 ="'" + sys.argv[1] + "'"


#input ="'" + input + "'"
#arg1 ="'" + arg1 + "'"

cur = conn.cursor()


if arg1 == "All":
  cur.execute("SELECT word, count from Tweetwordcount ORDER BY 1")
  records = cur.fetchall()
  conn.commit()
  for rec in records:
    print rec[0], rec[1]
    
else:
  pass


if arg1 != "All":
  cur.execute("SELECT word, count from Tweetwordcount WHERE word =%s" %arg1)
  records = cur.fetchall()
  conn.commit()
  for rec in records:
    print "Total number of occurences of", rec[0],":", rec[1]
else:
  pass


conn.close()


