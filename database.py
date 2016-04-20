import sqlite3 as lite
import pandas as pd

cities = (('Las Vegas', 'NV'), ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'), ('Atlanta', 2013, 'July', 'January',))

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('get_started.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text)")
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)
    cur.execute("SELECT * FROM weather LEFT OUTER JOIN cities ON city = name WHERE warm_month IS 'July'")

    rows = cur.fetchall() #grabbing all the rows
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

print(df)