import sqlite3 as lite

con = lite.connect('get_started.db')

# Inserting rows by passing values directly to `execute()`
with con:

    cur = con.cursor()
    #cur.execute("CREATE TABLE cities (name text, state text)")
    #cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text)")
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', NULL)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', NULL)")