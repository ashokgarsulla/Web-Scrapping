# Import required modules
import csv
import sqlite3
import datetime 

# Connecting to the geeks database
db_name = str(datetime.date.today()).replace("-","")+"_verge"+".db"
connection = sqlite3.connect(db_name)

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE Post(
				id INTEGER PRIMARY KEY  ,
				url TEXT NOT NULL,
				headline TEXT NOT NULL,
				author TEXT NOT NULL,
				date TEXT NOT NULL);
				'''

# # Creating the table into our
# # database
cursor.execute(create_table)

# Opening the person-records.csv file
file = open('20220902_verge.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)



# SQL query to insert data into the
# person table
insert_records = "INSERT INTO Post (id,url, headline, author, date) VALUES(?, ?, ?, ?, ?)"

# # Importing the contents of the file
# # into our person table
cursor.executemany(insert_records, contents)

# # SQL query to retrieve all data from
# # the person table To verify that the
# # data of the csv file has been successfully
# # inserted into the table
select_all = "SELECT * FROM Post"
rows = cursor.execute(select_all).fetchall()

# # Output to the console screen
for r in rows:
	print(r)

# # Committing the changes
connection.commit()

# # closing the database connection
connection.close()
