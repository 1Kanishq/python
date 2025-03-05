# class School:
#     School_name='S.T. Thomas'
#     aaddr = 'sahibabad'
#     principal ='Mr.Dious'

#     def __init__(self,a,b,c): # It is use to initialize the object properties
#         self.sname =a
#         self.rollno = b
#         self.addr = c
#     def std_info(self):
        # print(f'name of the student{self.ename}, rollno of the student is{self.rollno}\n, address is {self.addr}')
# std1 =School('Anshul',20,'ayoudhya')
# std2 =School('Kanishq',20,'Ghaziabad')

# print(std1.sname)
# print(std1.rollno)
# print(std1.addr)

class School:
    School_name='S.T. Thomas'
    aaddr = 'sahibabad'
    principal ='Mr.Dious'

    def __init__(self):
        self.sname =eval(input("Enter the name: "))
        self.rollno = eval(input("Enter the rollno: "))
        self.addr = eval(input("Enter the address: "))
std1 = School()

print("Details of the student")
print(f'Name of the student is {std1.sname}')
print(f"Name of the rollno is {std1.rollno}")
