import sqlite3 as lite
import pandas as pd 

con = lite.connect('get_started.db') #creates an object with connection to database

with con:

	cur = con.cursor() # this creates a cursor object
	cur.execute("SELECT * FROM cities") #grabs all columns from cities table

	rows = cur.fetchall() #grabbing all the rows
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)

	
	print(df)


	