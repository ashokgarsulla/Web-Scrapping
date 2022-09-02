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



table_exists = 0

sql_query = """SELECT name FROM sqlite_master
WHERE type='table';"""


# executing our sql query
cursor.execute(sql_query)
tables = cursor.fetchall()
for i in tables:
    for j in i:
        if j == "Post":
            table_exists = 1 

if table_exists == 0:
    cursor.execute(create_table)

file = open('20220902_verge.csv')
contents = csv.reader(file)
print("contents")
print(type(contents))
data = []
for i in contents:
    data.append(i)
print(data[-1])
# insert_records = "INSERT INTO Post (id,url, headline, author, date) VALUES(?, ?, ?, ?, ?)"
# cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM Post Order By id DESC"
rows = cursor.execute(select_all).fetchall()



# Output to the console screen
# for r in rows:
# 	print(r)


print(type(rows))
# print(rows)

print(rows[1][0])

# # Committing the changes
connection.commit()

# # closing the database connection
connection.close()
