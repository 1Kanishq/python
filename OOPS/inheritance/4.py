class HighSchool:
    Sname = 'S.T Thomas'
    Sloc = 'Sahibabad'

    def __init__(self,name,phno,hrollno,hYOP,hpercent):
        self.name = name
        self.phno = phno
        self.hrollno = hrollno
        self.hYOP = hYOP
        self.hpercent = hpercent

    def display_info(self):
        print('name:',self.name)
        print('phone:',self.phno)
        print('hrollno:',self.hrollno)
        print('H_YOP:',self.hYOP)
        print('H_Percentage:',self.hpercent)

class Intermediate(HighSchool):
    Sname = 'S.T Thomas'
    Sloc = 'Indrapuram'

    def __init__(self, name, phno, hrollno, hYOP, hpercent,ipercent,iYOP,irollno):
        super().__init__(name, phno, hrollno, hYOP, hpercent)
        self.ipercent = ipercent
        self.iYOP = iYOP
        self.irollno = irollno

    def display_info(self):
        super().display_info()
        print(self.ipercent, self.irollno, self.iYOP)

class College(Intermediate):
    Cname = 'KEC'
    Cloc = 'Mohan Nagar'

    def __init__(self, name, phno, hrollno, hYOP, hpercent, ipercent, iYOP,cpercent,cYOP,crollno):
        super().__init__(name, phno, hrollno, hYOP, hpercent, ipercent, iYOP)
        self.cpercent = cpercent
        self.cYOP = cYOP
        self.crollno = crollno
    
    def display_info(self):
        super().display_info()
        print(self.crollno,self.cpercent)

obj1 = College('Kanishq', 9312126845,596052,2019,80)
obj2 = Intermediate()
x = College()

x.display_info()