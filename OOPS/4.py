#WAP to take a claass bank with minimum 3 static members and 2objects with atleast 5 object members
class bank:
    bname='SBI'
    bloc='sec-16'       # Static Members
    bIFSC='SBIN0030933'
rhythm=bank()
kanishq=bank() # Objects 

rhythm.name='rhythm'
rhythm.accno=232354838411
rhythm.phoneno=8723434523
rhythm.addr='Ashok nagar'
rhythm.PAN='DHAGDbd134343'

kanishq.name='Kanishq'      #Object members
kanishq.accno=4325456354655
kanishq.phone=9312126846
kanishq.addr='Mohan Nagar'
kanishq.PAN='FGHJk23223'


print(bank.bname,bank.bIFSC,bank.bloc)
print(rhythm.name,rhythm.accno,rhythm.PAN)
print(kanishq.name,kanishq.phone,kanishq.PAN,kanishq.addr)

