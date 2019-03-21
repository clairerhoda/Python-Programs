#Claire Rhoda
#1068768
#Program 6
#This program calculates the sum of single-digit numbers
#sequentially entered by the user

def string_total(number_strings:str)->int:
    sum = 0
    for numbers in number_strings:
        sum += int(numbers) 
    return sum

def main():
    number_string = input("Enter a sequence of digits with nothing separating them: ")
    total = string_total(number_string)
    print("The total of the digits in the string you entered is",total)

if __name__ == "__main__":
    main()
