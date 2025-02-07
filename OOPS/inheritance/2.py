# Drive sigle level inheritance of online and offline bank

class online_Bank:
    bname= "kodak"
    bIFSC="Kodak3726r62tr"
    bhelpno = 9856844848

    def __init__(self,name,PAN,add,email):
        self.name = name
        self.PAN = PAN
        self.add = add
        self.email = email

    def disp_info(self):
        print('name',self.name)
        print('PAN no.',self.PAN)
        print('address',self.add)
        print('email',self.email)

class offline(online_Bank):
    def __init__(self, name, PAN, add, email,aadhar,phno,):
        super().__init__(name, PAN, add, email)
        self.aadhar = aadhar
        self.phno = phno

    def disp_info(self):
        super().disp_info()
        print(self.aadhar,self.phno)
    
obj = offline("Kanishq",'KFKEBII12323','Ghaziabad','example@gmail.com',842105515760,9319589923)

obj.disp_info()