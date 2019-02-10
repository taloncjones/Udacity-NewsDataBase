# "Database code" for the news DB.

import psycopg2

DB_name = "news"


def top_art():
    # Return top three news articles of all time.
    db = psycopg2.connect(database=DB_name)
    c = db.cursor()
    c.execute('''select articles.slug, count(*) as num
      from articles
      join log on log.path like '%' || articles.slug || '%'
      group by articles.slug
      order by num desc
      limit 3;''')
    topthree = c.fetchall()
    db.close()
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
    return higherror
