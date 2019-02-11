#!/usr/bin/env python3

# "Database code" for the news DB.

import psycopg2

DB_name = "news"


def top_art():
    # Return top three news articles of all time.
    db = psycopg2.connect(database=DB_name)
    c = db.cursor()
    c.execute('''select articles.title, count(*) as num
      from articles
      join log on log.path like '%' || articles.slug || '%'
      group by articles.title
      order by num desc
      limit 3;''')
    topthree = c.fetchall()
    db.close()
    print('Top 3 Articles:')
    for row in topthree:
        x, y = row
        print('Article: %s\t Article Views: %s' % (x, y))
    return topthree


def top_auth():
    # Return top authors of all time.
    db = psycopg2.connect(database=DB_name)
    c = db.cursor()
    c.execute('''select authors.name, count(*) as num
      from articles
      join log on log.path like '%' || articles.slug || '%'
      join authors on articles.author = authors.id
      group by authors.name
      order by num desc;''')
    topauth = c.fetchall()
    db.close()
    print('Top Authors:')
    for row in topauth:
        x, y = row
        print('Author: %s\t Total Article Views: %s' % (x, y))
    return topauth


def high_error():
    # Return days where >1% of requests had errors.
    db = psycopg2.connect(database=DB_name)
    c = db.cursor()
    c.execute('''select total.date,
        round(100 * (err.errors::decimal / (total.total + err.errors)), 2)
        as percentfailure
      from (select date_trunc('day', log.time) as date, count(*) as total
        from log where log.method = 'GET' group by date) as total
      join (select date_trunc('day', log.time) as date, count(*) as errors
        from log where log.status != '200 OK' group by date) as err
      on total.date = err.date
      where round(100 * (err.errors::decimal / (total.total + err.errors)), 2)
         > 1
      order by percentfailure desc;''')
    higherror = c.fetchall()
    db.close()
    print('High Error Days:')
    for row in higherror:
        x, y = row
        print('Date: %s\t Error %%: %s' % (x, y))
    return higherror


# Selector dictionary for above functions
selector = {
    'articles': top_art,
    'authors': top_auth,
    'errors': high_error
}


# Introduction text when program starts
intro = '''Welcome to the News Database!
Type 'articles' to view the top 3 articles in the database.
Type 'authors' to view the top authors.
Type 'errors' to view days that the error percentage exceeded 1%.
Type 'exit' to exit the program'''


# Main function
if __name__ == "__main__":
    print(intro)
    choice = ''
    # Until user types 'exit', keep asking for input
    while choice != 'exit':
        choice = input('> ').lower()
        try:
            selector[choice]()
        # If input is not a call to top_art, top_aut, high_error, or exit
        except KeyError:
            if choice != 'exit':
                print('Not a valid option.')
