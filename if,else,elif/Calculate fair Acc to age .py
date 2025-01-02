age = int(input("Enter the age"))
if 6<=age<=12:
    print("childen fair ---- Rs 1000")
elif 13<=age<=19:
    print("Teenager fair ---- RS 1200")
elif 20<=age<=50:
    print("Adult fair ---- Rs 1400")
elif age>50:
    print("Senior Citizen fair ----- Rs500")
else:
    print("Not Allowed")
