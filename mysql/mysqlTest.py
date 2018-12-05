#!/usr/bin/python3
import pymysql

# create connection
db = pymysql.connect('localhost', 'root', '123456', 'test_db')

# create cursor
cursor = db.cursor()

#execute sql
cursor.execute("SELECT VERSION()")

# fetchone get data
data = cursor.fetchone()

print ("Database version : %s " % data)


# SQL insert data
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""


try:
	cursor.execute(sql)
	db.commit()
except Exception as e:
	print('exection', e)
	db.rollback()


# SQL select
sql2 = "SELECT first_name, last_name, age, sex, income FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)	

try:
	cursor.execute(sql2)
	results = cursor.fetchall()
	
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		# print result
		print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except Exception as e:
	print("select exception:", e)
	
# SQL update
sql3 = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')


try:
	cursor.execute(sql3)
	db.commit()
except Exception as e:
	print("update exception happen", e)
	db.rollback()
	
sql4 = "DELETE FROM EMPLOYEE WHERE id < '%d'" % (1)
try:
	cursor.execute(sql4)
	db.commit()
except Exception as e:
	print("update exception happen", e)
	db.rollback()
#colse the connection
db.close()