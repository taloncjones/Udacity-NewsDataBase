# "Database code" for the news DB.

import psycopg2
import bleach

DB_name = "news"

def top_art():
  """Return top three news articles of all time."""
#  db = psycopg2.connect(database=DB_name)
#  c = db.cursor()
#  c.execute("select content, time from posts order by time desc;")
#  posts = c.fetchall()
#  db.close()
  return top

def top_auth():
  """Return top authors of all time."""
#  db = psycopg2.connect(database=DB_name)
#  c = db.cursor()
#  c.execute("select content, time from posts order by time desc;")
#  posts = c.fetchall()
#  db.close()
  return top

def high_error():
  """Return days where >1% of requests had errors."""
#  db = psycopg2.connect(database=DB_name)
#  c = db.cursor()
#  c.execute("select content, time from posts order by time desc;")
#  posts = c.fetchall()
#  db.close()
  return top

