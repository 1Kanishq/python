class bank:
    bname='HDFC'
    bloc='saket'
    bIFSC='HDFC357334SS'


    def __init__(self,name,phno,email,accno):
        self.name=name
        self.phno=phno
        self.email=email
        self.accno=accno

jyoti=bank('jyoti',9554613438,'kuchbhi123@gmail.com',55654845443)

print(jyoti.email,jyoti.bIFSC)