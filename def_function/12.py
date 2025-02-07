#   Function with return
# output : {'p':['Python','programming],'i':['is'],'l':['Language']}
def funct1():
    a='python is programing language'
    out={}
    a=a.split()
    for i in a:
        if i[0] not in out:
            out[i[0]]=[i]
        else:
            out[i[0]]+=[i]
    return out
print(funct1()) 