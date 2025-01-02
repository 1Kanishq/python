def funct_name():
    a=[10,'Hai',25,'Hai',3+5j,10,'Hello',10]
    #op=[10,'Hai']
    out=[]
    for i in a:
        if i not in out:
            if a.count(i)>1:
                out+=[i]
    print(out)
            
