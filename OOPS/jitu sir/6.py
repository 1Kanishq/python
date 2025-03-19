class School:
    School_name='S.T. Thomas'
    aaddr = 'sahibabad'
    principal ='Mr.Dious'

    def __init__(self,a,b,c): # It is use to initialize the object properties
        self.sname =a
        self.rollno = b
        self.addr = c
    def std_info(self):
        print(f'name of the student{self.sname}, rollno of the student is{self.rollno}\n, address is {self.addr}')

    def change_addr(self):
        self.addr =eval(input("Enter the new address: "))

    @classmethod
    def school_info(cls):
        print(f'School name is {cls.School_name},principal of the school is {cls.principal},address is {cls.addr}')
        
    @classmethod
    def change_principal(cls,new):
        cls.principal = new

std1 =School('Anshul',20,'ayoudhya')
std2 =School('Kanishq',20,'Ghaziabad')
std1.std_info()
print('School information---')
School.school_info()

