Author: Talon Jones

Welcome to my implementation of newsdb.py. This program's intended purpose is to
perform one of three psql requests to the news database as part of the UDACITY -
Full Stack course. The three requests are:
 - Get the top 3 articles by view count. Return title and view count.
 - Get the top authors by article view count. Return name and total views.
 - Get the days with HTTP GET errors exceeding 1% of all requests. Return date and error %.


## Intended usage is with:
```python3 newsdb.py```


## Steps to set up:
```
## Install dependencies.
apt-get -qqy install make zip unzip postgresql

apt-get -qqy install python3 python3-pip
pip3 install --upgrade pip
pip3 install flask packaging oauth2client redis passlib flask-httpauth
pip3 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests

apt-get -qqy install python python-pip
pip2 install --upgrade pip
pip2 install flask packaging oauth2client redis passlib flask-httpauth
pip2 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests

## Create news DB and import news database. Replace <username> with desired username.
su postgres -c 'createuser -dRS <username>'
su <username> -c 'createdb'
su <username> -c 'createdb news'
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
su <username> -c 'psql news -f newsdata.sql'
```


## Expected output:
```
$ python3 newsdb.py 
Welcome to the News Database!
Type 'articles' to view the top 3 articles in the database.
Type 'authors' to view the top authors.
Type 'errors' to view days that the error percentage exceeded 1%.
Type 'exit' to exit the program.
> articles
Top 3 Articles:
Article: Candidate is jerk, alleges rival        Article Views: 338647
Article: Bears love berries, alleges bear        Article Views: 253801
Article: Bad things gone, say good people        Article Views: 170098
> authors
Top Authors:
Author: Ursula La Multa  Total Article Views: 507594
Author: Rudolf von Treppenwitz   Total Article Views: 423457
Author: Anonymous Contributor    Total Article Views: 170098
Author: Markoff Chaney   Total Article Views: 84557
> errors
High Error Days:
Date: 2016-07-17 00:00:00+00:00  Error %: 2.26
> exit
```

## Overview:
```
#!/usr/bin/env python3

import psycopg2

DB_name = "news"
```

#### def connect_db():
##### Try to connect to DB_name, or return error and exit
 1. Attempt to connect to DB_name
 2. On error, report error and exit
 3. Return db connection

#### def top_art():
##### Return top 3 news articles based on view count
 1. Call connect_db()
 2. Send psql query
 3. Print Article Titles\t View Count
 4. Return topthree

#### def top_auth():
##### Return top authors based on article view count
 1. Call connect_db()
 2. Send psql query
 3. Print Author Name\t Total View Count
 4. Return topauth

#### def high_error():
##### Return days with HTTP GET requests resulting in errors >1%
 1. Call connect_db()
 2. Send psql query
 3. Print Date\t Error %
 4. Return higherror

#### Selector dictionary for above functions
```
selector = {
}
```

#### Introduction text when program starts
```
intro = ''' '''
```

#### Main function
```
if __name__ == "__main__":
    print(intro)
    # Until user types 'exit', keep asking for input
        # If input is not a call to top_art, top_aut, high_error, or exit
                print('Not a valid option.')
```
