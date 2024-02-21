import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root")
db_cursor=mydb.cursor()

db_cursor.execute("select * from learnpython.emp")
#to fetch the data in a single line 
#db_select=db_cursor.fetchall()
#print(db_select)

#to fetch the data in a next line one by one
for db_data in db_cursor.fetchall():
    print(db_data)