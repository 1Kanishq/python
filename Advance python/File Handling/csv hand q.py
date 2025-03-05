# Create a file to store data of student by using oop and file handling.

import csv
var=open('student_data.py','w')
a = csv.writer(var)
a.writerow(['std_name','rollno','subject'])

class School:
    def __init__(self,name,roll,sub):
        self.name = name
        self.roll = roll
        self.sub= sub
        a.writerow([self.name,self.roll,self.sub])
s1 =School('Parnika',21,'pyh')
s2 =School('Kanishq',22,'java')
s3 =School('Simran',23,'sql')
var.close()
