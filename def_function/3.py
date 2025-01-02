def fname():
    x='1010030$10A'
   #OP='01011#1#01#'
    op=''
    for i in x:
        if i=='0':
            op+='1'
        elif i=='1':
            op+='0'
        else:
            op+='#'
    print(op)
fname()
