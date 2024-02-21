import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root")
db_cursor=mydb.cursor()
db_deletedata="delete from learnpython.emp where ename=%s"
db_value=("Reem",)
db_cursor.execute(db_deletedata,db_value)
mydb.commit()
print(db_cursor.rowcount,"Record deleted....")