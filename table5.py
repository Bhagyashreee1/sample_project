import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root",database="learnpython")
db_cursor=mydb.cursor()

#db_cursor.execute("create table emp(id int,ename varchar(20))")
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)