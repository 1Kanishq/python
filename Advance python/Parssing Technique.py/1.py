# In JASON Module the data is formated in the form of string

# import json
# enc_data= json.dumps(org_data)

import json
list1=[10,20,30]
enc_data=json.dumps(list1)

with open('storage.txt','w')as f:
    f.write(enc_data)

print(enc_data,type(enc_data))

# 2

var=open('storage.txt','r')
org_data=var.read()
res=json.loads(org_data)
print(res,type(res))
