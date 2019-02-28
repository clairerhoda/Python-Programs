import random
user_num = 0.0
lottery_num = random.randint(10,99)
#input
while user_num != -999:
    user_num = int(input("Enter a two digit number: "))
    user1stDigit = user_num // 10
    user2ndDigit = user_num % (10)
    lottery1stDigit = lottery_num // 10
    lottery2ndDigit = lottery_num % (10)
    if user_num == lottery_num:
        print("You got all the right digits! + $10000")
    elif lottery2ndDigit == user1stDigit and lottery1stDigit == user2ndDigit:
        print("You match the digits but not the order +$3000")
    elif lottery2ndDigit == user2ndDigit or user1stDigit == lottery1stDigit or user1stDigit == lottery2ndDigit or user2ndDigit == lottery1stDigit:
        print("You got one of the digits correct +$1000")
print("Kill Program")








