from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
     
    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        self.counts[word] += 1
	
        self.emit([word, self.counts[word]])
	self.log('%s: %d' % (word, self.counts[word]))
	self.conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")
        cur = self.conn.cursor()
         
          	
        repeat_w = False
	cur.execute("SELECT word, count from tweetwordcount")
        self.conn.commit()
	records = cur.fetchall()
	for rec in records:
          if rec[0] == word:
            repeat_w = True 
          else:
	    pass
  

        if repeat_w == True:
          cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (rec[1] + self.counts[word], word)) 
	else:        
          cur.execute("INSERT INTO tweetwordcount (word,count) \
             VALUES (%s, %s)", (word, self.counts[word]))     
         	
        self.conn.commit()
	self.conn.close()
        self.counts[word] = 0 
        
