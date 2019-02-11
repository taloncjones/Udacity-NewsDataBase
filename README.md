Author: Talon Jones

Welcome to my implementation of newsdb.py. This program's intended purpose is to
perform one of three psql requests to the news database as part of the UDACITY -
Full Stack course. The three requests are:
 - Get the top 3 articles by view count. Return title and view count.
 - Get the top authors by article view count. Return name and total views.
 - Get the days with HTTP GET errors exceeding 1% of all requests. Return date and error %.


Intended usage is with:
 - python3 newsdb.py


Expected output:
 - $ python3 newsdb.py 
   Welcome to the News Database!
   Type 'articles' to view the top 3 articles in the database.
   Type 'authors' to view the top authors.
   Type 'errors' to view days that the error percentage exceeded 1%.
   Type 'exit' to exit the program
   > articles
   Top 3 Articles:
   Article: Candidate is jerk, alleges rival        Article Views: 342102
   Article: Bears love berries, alleges bear        Article Views: 256365
   Article: Bad things gone, say good people        Article Views: 171762
   > authors
   Top Authors:
   Author: Ursula La Multa  Total Article Views: 512805
   Author: Rudolf von Treppenwitz   Total Article Views: 427781
   Author: Anonymous Contributor    Total Article Views: 171762
   Author: Markoff Chaney   Total Article Views: 85387
   > errors
   High Error Days:
   Date: 2016-07-17 00:00:00+00:00  Error %: 2.21
   > exit


Overview:
#!/usr/bin/env python3

import psycopg2

DB_name = "news"

# Return top 3 news articles based on view count
def top_art():
 - Connect to database "news"
 - Send psql query
 - Print Article Titles\t View Count
 - Return topthree

# Return top authors based on article view count
def top_auth():
 - Connect to database "news"
 - Send psql query
 - Print Author Name\t Total View Count
 - Return topauth

# Return days with HTTP GET requests resulting in errors >1%
def high_error():
 - Connect to database "news"
 - Send psql query
 - Print Date\t Error %
 - Return higherror

# Selector dictionary for above functions
selector = {
}

# Introduction text when program starts
intro = ''' '''

# Main function
if __name__ == "__main__":
    print(intro)
    # Until user types 'exit', keep asking for input
        # If input is not a call to top_art, top_aut, high_error, or exit
                print('Not a valid option.')
