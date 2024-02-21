import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root",database="learnpython")
db_cursor=mydb.cursor()
db_insert="insert into emp(id,ename) values(%s,%s)"
db_list=[(12,"Pooja"),(13,"Geeta"),(14,"Reem")]
db_cursor.executemany(db_insert,db_list)
#db_cursor.execute("insert into emp(id,ename) values(%s,%s)",(11,"Pragya"))
mydb.commit()
print(db_cursor.rowcount,"Record inserted......")