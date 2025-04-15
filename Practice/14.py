lt=[12,30,400,'60']
ct=1
for i in range(len(lt)-1):
    if type(lt[i])== type(lt[i+1]):
        ct+=1
    else:
        print("Hetrogeneous")
if ct==len(lt):
    print("Homogeneous")