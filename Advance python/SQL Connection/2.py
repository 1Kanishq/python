import sqlite3
var=sqlite3.connect('employee.db')
a=var.cursor()
# a.execute("create table employee('Ename','Esal','Phno')")
a.execute("insert into employee values('Mohit','112312','6764713849')")
a.execute("insert into employee values('Kanishq','8000015','9319589923')")
a.execute("insert into employee values('abhishek','1001022','7394433113')")
var.commit()
var.close()