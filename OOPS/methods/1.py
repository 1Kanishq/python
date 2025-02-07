# methods in OOPs:
    # These are some functions which are use to add data, access the data, modify the data inside the class and object.
    # We have 3 types of methods

    # 1. ---> Object method
    # 2. ---> class method
    # 3. ---> Static method

#Object method#:=These are the methods which are use to modify,access the object property present inside the class.


class TY:
    cname='PySP'
    cloc='sec-3'
    addr='B-4,near metro-16'

    def __init__(self,name,phno,addr,email,YOP,stream,MOCk):
        self.name=name
        self.phno=phno
        self.addr=addr
        self.email=email
        self.YOP=YOP
        self.stream=stream
        self.MOCk=MOCk
    def disp_obj(self):
        print(self.name,self.phno,self.addr,self.email,self.YOP,self.stream,self.MOCk)
    
    
    def ch_phno(self,new):
        self.photo=new
    
    def ch_MOCK(self,new):
        self.MOCk=new

himashu=TY('himanshu',92355454248,'delhi','email@gmail.com',2023,'CSE',1)
kanishq=TY('Kanishq',9319589923,'Mohan Nagar','kanishqyadav00@gmail.com',2025,'CSE(A.I)','1*')

himashu.disp_obj()   #  obj.methodname() ----> To Access
himashu.ch_MOCK(2)   #  obj.methodname(Value) -----> To Modify
himashu.disp_obj()   #  Modified



