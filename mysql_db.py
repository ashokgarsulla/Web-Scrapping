import csv
import mysql.connector as mysql

dataBase = mysql.connect(
  user ="root",
  password ="1234567890",
  host ="127.0.0.1",
  port = "3306",
  database = "web_scraping",
)

cursor_obj = dataBase.cursor()
# # creating database
# # cursor_objObject.execute("CREATE DATABASE web_scraping")


# create_table = '''CREATE TABLE Post(
# 				id INT PRIMARY KEY  ,
# 				url VARCHAR(200) NOT NULL,
# 				headline VARCHAR(200) NOT NULL,
# 				author VARCHAR(50) NOT NULL,
# 				date VARCHAR(20) NOT NULL);
# 				'''


# table_exists = 0

# sql_query = "SHOW TABLES"


# # executing our sql query
# cursor_obj.execute(sql_query)
# tables = cursor_obj.fetchall()
# print(type(tables))
# for i in tables:
#   print(type(i[0]))
#   if i[0] == 'Post':
#     table_exists = 1 


# print(table_exists)
# # if table_exists == 0:
# #     cursor_obj.execute(create_table)


file = open('20220902_verge.csv')
contents = csv.reader(file)
# print("contents")
# print(type(contents))
# data = []
# for i in contents:
#     data.append(i)
# print(data[-1])
val  = []
for i in contents:
  val.append(tuple(i))

# for i in val:
#   print(i)

# insert_records = "INSERT INTO post(id, url, headline, author, date) VALUES(%s, %s, %s, %s, %s)"
# val = (1, "COKJGU90NTPU4JMPERMKRPOSE", "DWNKJCNSDLCNSLSD", "VBDFKVNBDFKVNK", "CSDVDFVFD")
# # cursor_obj.executemany(insert_records, val)
# cursor_obj.execute(insert_records, val)
# select_all = "SELECT * FROM Post "
# cursor_obj.execute(select_all)
# rows = cursor_obj.fetchall()
# # for i in rows:
# #   print(i)


cursorObject = dataBase.cursor()
  
# creating table
# studentRecord = """CREATE TABLE POST2 (
#                    ID  INT PRIMARY KEY,
#                    URL VARCHAR(250),
#                    HEADLINE  VARCHAR(250),
#                    AUTHOR VARCHAR(50),
#                    DATE VARCHAR(50)
#                    )"""
  
# # table created
# cursorObject.execute(studentRecord)
  
# disconnecting from server
# dataBase.close()


sql = "INSERT INTO POST2 (ID, URL, HEADLINE, AUTHOR, DATE) VALUES (%s, %s, %s, %s, %s)"
# val = ("Ram", "CSE", "85", "B", "19")
   
cursorObject.executemany(sql, val)
dataBase.commit()

# disconnecting from server
dataBase.close()