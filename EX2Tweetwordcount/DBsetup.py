

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="", host="localhost", port="5432")

cur = conn.cursor()
cur.execute('CREATE DATABASE ' + "Nano")
cur.close()
conn.close()


conn = psycopg2.connect(database="postgres", user="postgres", password="", host="localhost", port="5432")
cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       ((word varchar(100), count integer);''')
conn.commit()
conn.close()


