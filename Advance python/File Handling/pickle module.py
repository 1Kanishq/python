# Dump :- Used to Write data into binary file

# Syntax : - pickle.dump(data,for)
import pickle
# F=open("employee.json","wb")
# empno=input("Enter the number")
# empname =input("Enter the name")
# empsal=int(input("Enter the sal"))
# pickle.dump([empno,empname,empsal],F)
# F.close()
def disp():
    F1=open("employee.json","rb")
    x=pickle.load(F1)
    print(x)
    F1.close()
disp()