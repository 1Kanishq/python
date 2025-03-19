# SQL Connection
# Its a process where user can interact with the database easily.
# we use (import sqlite3)
# i) Connet() : It is use to conect with the database.
# ii) cursor() : It is use to make the controler get pointed to a particular position in a database.
# iii) execute(): this function helps us to write and execute the excel queries.
# iv) commit(): It is use to save the changes that are done in the database.
# v) close(): It is used to disconnect from the database. 

import sqlite3
var= sqlite3.connect('student.db')
a = var.cursor()
a.execute("create table student('sname','roll','addr')")
a.execute("insert into student values('Kanishq','28','ghaz')")
a.execute("insert into student values('Mohit','29','ghz')")
a.execute("insert into student values('Rohit','30','abc')")
var.commit()
var.close()

