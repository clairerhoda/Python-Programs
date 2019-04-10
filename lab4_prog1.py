def main():
    brics = ['Brazil','Russia','India','China','Sri Lanka']
    again = "Y"
    while again.upper() == "Y":
        guess = input("Enter the name of a country:")
        valid = guessCheck(guess,brics)
        if valid == True:
            print(guess,"is a member of BRICS")
        elif valid == False:
            print(guess,"is not a member of BRICS")
        print("Do you want to enter another country?")
        again = input("y = yes, anyhting else = no")

def guessCheck(guess:str,brics:list)->bool:
    if guess in brics:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
