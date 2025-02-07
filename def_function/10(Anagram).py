# These are the numbers whose sum by the no.of digits,pair no.of digits power where individual value will be sum which is equal the same number
# do it while loop and for Loop  ex: 153= 1^3+5^3+3^3

def fun1(num):
    summ=0
    i=len(str(num))-1
    while i>=0:
        ld = num%10
        summ= summ + ld(str(num)) 
        print(summ)
        num = num//10
        i-=1
    if summ == num:
        print("Its An Anagram")
    else:
        print("Its Not")
    print(summ)

fun1(153)

