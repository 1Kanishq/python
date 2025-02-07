class bank:     # Class declaration
    bname='Kodak'
    bloc='meerut'
    bIFSC='Kodak003219338812'

    def sam(obj,name,addr,phno,addhar,PAN,email):   # Function declared inside the class bank
        # Object Members
        obj.name=name
        obj.addr=addr
        obj.phno=phno
        obj.addhar=addhar
        obj.PAN=PAN
        obj.email=email
    # Object creation
Kanishq=bank()  
Babu=bank()
# Object Members values declaration 
Kanishq.sam('kanishq','Ghaziabad',9319589923,842105515430,'KQUZJ7483','kanishqyadav008@gmail.com') 
Babu.sam('BabuBhaiya','sec-16',987456315,788454465484,'FHAHGD325436','babudon@gmail.com')

print(bank.bIFSC,Kanishq.addhar,Babu.name)
