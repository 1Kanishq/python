# RE ~~~ 

import re

data = 'This is 05000040403 we have 0938983477 3423 3434 32 99990491615 7826789923'
phno=re.findall('[6-9][0-9]{9}',data) # [6-9] will see that nubmer should start with 6-9. [0-9]{n} it will search till n number  
print(phno)

data1 = 'This is 4000000232343 python sky eye havass 30-12-2025 12-05-2024 18-10 python123@gmail^com'
email = re.findall('\w*@\w*.[a-z]{2,3}',data1) # for ^ to negect it we use '\'
print(email)