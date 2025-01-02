luck_num=13
while True:
    bet=int(input("Bet the Number"))
    if bet>luck_num:
        print("koi nhi bhai hota hai")
    elif bet<luck_num:
        print("Chota rahe gaya")
    else:
        print("Bhadai ho")
        break