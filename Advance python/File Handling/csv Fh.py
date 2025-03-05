import csv
var = open('hh.py','w')
a = csv.writer(var)
a.writerow(['Eid','Ename','Esal','Eaddr'])
a.writerows([['Hello Mohit ','How are you'],[101,'Kanishq',800000,'Mohan Nagar'],[102,'Rawat',120000,'Phar ki choti']])
var.close()

var = open('hh.py','r')
a=csv.reader(var)
print(a)
print([i for i in list(a)[1:] if i!=[]])