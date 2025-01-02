user='kuchbhi123'
password='@15432'
while True:
    user_id=input("Enter the Username")
    pass1=input("Enter the Password")
    if user_id==user and password==pass1:
        print("Welcome")
        break
    else:
        print("enter the proper id or password")
