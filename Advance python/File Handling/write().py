# File Handling

var=open(r'C:\Users\AAKASH\Desktop\Fh.py','w')
data1 = 'Good Afternoon\n'
data2 = 'How are u\n'
data3 = 'what a re u doing\n'
print(var.write(data1))
print(var.writelines([data2,data3])) #To add multipleline in the file we use list
var.close()
# print(var.writelines([data1]))
# print(var.writelines([data1,data2,data3]))
