#WAP to extract all the uperrcase from the given string
def Upper_case():
    a='SBDbCjdvsDVdvdDvjdJV'
    out=''
    for i in range(len(a)):
        if 'A'<=a[i]<='Z':
            out+=a[i]
    print(out)
Upper_case()
