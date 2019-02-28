import random
count = 0
choices = ["rock","paper","scissors"]
while count < 2 and count > -2:
    computer = random.randint(0,2)
    computerchoice = choices[computer]
    userChoice = input("Enter rock, paper, scissors")
    if computerchoice == "rock":
        if userChoice == "rock":
            print("Draw")
        elif userChoice == "paper":
            print("You won")
            count = count + 1
        elif userChoice == "scissors":
            print("You loose")
            count = count - 1
    elif computerchoice == "paper":
        if userChoice == "rock":
            print("You loose")
            count = count - 1
        elif userChoice == "paper":
            print("Draw")
        elif userChoice == "scissors":
            print("You won")
            count = count + 1
                                 elif computerchoice == "scissors":
        if userChoice == "rock":
            print("You won")
            count = count + 1
        elif userChoice == "paper":
            print("You loose")
            count = count - 1
        elif userChoice == "scissors":
            print("Draw")      
    print(count)
if count > 0:
    print("You won more than 2 times")
else:
    print("The computer wins by more than 2")
