import csv
import mysql.connector

connection = mysql.connector.connect(
  user ="root",
  password ="1234567890",
  host ="127.0.0.1",
  port = "3306",
  database = "web_scraping",
)

cursor = connection.cursor()
# creating database
# cursorObject.execute("CREATE DATABASE web_scraping")


create_table = '''CREATE TABLE Post(
				id INTEGER PRIMARY KEY  ,
				url TEXT NOT NULL,
				headline TEXT NOT NULL,
				author TEXT NOT NULL,
				date TEXT NOT NULL);
				'''


table_exists = 0

sql_query = "SHOW TABLES"


# executing our sql query
cursor.execute(sql_query)
tables = cursor.fetchall()
print(type(tables))
for i in tables:
  print(type(i[0]))
  if i[0] == 'Post':
    table_exists = 1 


print(table_exists)
# if table_exists == 0:
#     cursor.execute(create_table)


file = open('20220902_verge.csv')
contents = csv.reader(file)
# print("contents")
# print(type(contents))
# data = []
# for i in contents:
#     data.append(i)
# print(data[-1])

insert_records = "INSERT INTO Post (id,url, headline, author, date) VALUES(?, ?, ?, ?, ?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM Post Order By id DESC"
rows = cursor.execute(select_all).fetchall()
