# WAP to create class company to private some employee details d

class company:
    cname='Q Spyders'
    cloc='noida sec-16'
    cprofit='Bhot zyada'

    def __init__(self,empname,empid,empsalary,empphno,empDOJ):
        self.empname=empname
        self.empid=empid
        self.empsalary=empsalary
        self.empphno=empphno
        self.empDOJ=empDOJ
    
    def disp_obj(self):
        print('empname',self.empname)
        print('empsalary',self.empsalary)
        print('empid',self.empid)
        print('empphno',self.empphno)
        