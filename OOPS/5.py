#create class hospital with 4 class members 2 objects and 7 object members
class Hospital:
    hname='Mayuri'       #  class member  Static in nature.
    hloc='krishna nagar' #  class member
    hphone=9653321452    #  class member
    hward=150            #  class member

Rawat = Hospital()      #   Object 
Mohit = Hospital()      #   Object

Rawat.name='Rawat Yadav'    #  object Members
Rawat.phone=9313569982      #  object Members
Rawat.wardno=123            #  object Members
Rawat.admitdate=12052019    #  object Members 
Rawat.location='Mojpur'     #  object Members
Rawat.Fname='Kanishq'       #  object Members
Rawat.mail='rawat69@gmail.com'  #  object Members

Mohit.name='Mohit Arora'
Mohit.wardno=125
Mohit.phone=5466546354
Mohit.aditdate=121224
Mohit.Fname='Kanishq'

print(Hospital.hloc,Hospital.hphone)
print(Rawat.Fname,Rawat.name,Rawat.phone)
print(Mohit.Fname,Mohit.name,Mohit.phone)
