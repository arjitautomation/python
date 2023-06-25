import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="123456",database="fullstack")
mycursor=mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)
