import pickle
var=open(r'employee.json',"wb")
data=input("Enter the data ")
pickle.dump(data,var)# data= value that has to be stored,var = file name
var.close()

