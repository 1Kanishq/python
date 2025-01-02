a = int(input("Enter the Input"))
i=2
while i<a:
    if a%i==0:
        print("Its not a prime number")
        break
    i+=1
if i==a:
    print("Its Prime ")