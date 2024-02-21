import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root")
db_cursor=mydb.cursor()
db_updatedata="update learnpython.emp set id=%s where ename=%s"
db_value=(15,"Reem")

db_cursor.execute(db_updatedata,db_value)
mydb.commit()
print(db_cursor.rowcount,"Data updated.....")