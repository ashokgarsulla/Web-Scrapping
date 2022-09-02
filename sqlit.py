import csv
import sqlite3
import datetime 
db_name = str(datetime.date.today()).replace("-","")+"_verge"+".db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
create_table = '''CREATE TABLE Post(
				id INTEGER PRIMARY KEY  ,
				url TEXT NOT NULL,
				headline TEXT NOT NULL,
				author TEXT NOT NULL,
				date TEXT NOT NULL);
				'''
cursor.execute(create_table)

file = open('20220902_verge.csv')
contents = csv.reader(file)

insert_records = "INSERT INTO Post (id,url, headline, author, date) VALUES(?, ?, ?, ?, ?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM Post"
rows = cursor.execute(select_all).fetchall()

# # Output to the console screen
# for r in rows:
# 	print(r)

# # Committing the changes
connection.commit()

# # closing the database connection
connection.close()
