#Claire Rhoda
#1068768
#Program 2
#This program checks if an inputed string is a palindrome

def isPalindrome(string:str)->bool:
    """calcualtes if inputed string is a palindrome"""
    low = 0
    high = len(string) - 1
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True

def main():
    """let's user input any string"""
    """determines if return is True or False to give answer"""
    string = input("Enter a String:")
    while string != '-1':
        answer = isPalindrome(string)
        if answer == True:
            print(string,"is a palindrome")
            string = input("Enter a String:")
        else:
            print(string,"is not a palindrome")
            string = input("Enter a String:")

if __name__ == "__main__":
    main()
