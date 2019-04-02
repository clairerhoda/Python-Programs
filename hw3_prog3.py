#Claire Rhoda
#1068768
#Program 3
#This program checks the validation of a credit card number

def isValid(creditNum:str)->bool:
    a = sumOfDoubleEvenPlace()
    z = sumOfOddPlace()
    b = getDigit()
    if len(creditNum) >= 13 and len(creditNum) <= 16:
        if b % 10 != 0:
            if creditNum[0] == 4 or creditNum[0] == 5 or \
                creditNum[0] == 6 or creditNum[0] == 37:
                return True
    return False
def sumOfDoubleEvenPlace(creditNum:str)->int:
    for i in range(len(creditNum) - 2,-1,-2):
        i += len(creditNum)
        a = int(creditNum[i]) * 2
        if a[:2] == True:
            a = a[0:] + a[1:]
        return a
            
    

def sumOfOddPlace(creditNum:str)->int:
    for i in range(len(creditNum) - 1,-1,-2):
        i += len(creditNum)
        return i
        
def getDigit(i:int,a:int):
    sumOfOdd(i)
    sumOfDoubleEvenPlace(a)
    b = i + a
    return b
        
        

def main():
    creditNum = input("Enter credit card number as a long interger")
    sumOfDoubleEvenPlace(creditNum)
    sumOfOddPlace(creditNum)
    validity = isValid(creditNum)
    if validity == True:
        print(creditNum,"is valid")
    else:
        print(creditNum,"is invalid")
    

if __name__ == "__main__":
    main()
