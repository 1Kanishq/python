from configparser import Error


age = int(input("Enter the age--"))
if age >= 50:
    print('Too early for marriage')
    raise Error('This is userdefined error')
elif age >=18:
    print('you can marry at any moment')

else:
    print('Sorry !! its too late for u')
    raise AgeErro55r('This is userdefined error')  # type: ignore