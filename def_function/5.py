def speed():
    a='python is prograamming language'.split()
    out={}
    for i in a:
        if i[0] not in out:
            out[i[0]]=[i]
        else:
            out[i[0]]+=[i]
    return out
print(speed())
