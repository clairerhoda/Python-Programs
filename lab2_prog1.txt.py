#Claire Rhoda
#1068768
#Program 1
#Program that determines whether a person is eligible to vote or not

#user inputs an age
age = int(input("Enter the age : "))

#process for determining the years until eligible to vote if younger than 18
yrs = (18) - (age)

#processing/output for determining if the age is younger or older or equal to 18
if (age >= 18):
    print("You are eligible to vote") #prints is eligible
else:
    print("You have to wait for another",yrs,"years to cast your vote")  #prints amount of years until eligible to vote

#ask user to kill program
input('\n\nPress the enter key to quit')


##Test Case 1
##>>>
##============= RESTART: /Users/clairerhoda/Documents/lab2tests.py =============
##Enter the age : 45
##You are eligible to vote
##
##
##Press the enter key to quit
##
##Test Case 2
##>>>
##============= RESTART: /Users/clairerhoda/Documents/lab2tests.py =============
##Enter the age : 14
##You have to wait for another 4 years to cast your vote
##
##
##Press the enter key to quit
##
##Test Case 3
##>>>
##============= RESTART: /Users/clairerhoda/Documents/lab2tests.py =============
##Enter the age : 18
##You are eligible to vote
##
##
##Press the enter key to quit


#Claire Rhoda
#1068768
#Program 2
#Program that finds whether the given number is even or odd

#user inputs any number
num = int(input("Enter any number : "))

#processing for even numbers
if (num % 2 == 0):
    print(num,"is even")

#processing for odd numbers
else:
    print(num,"is odd")

#ask user to kill program
input('\n\nPress the enter key to quit')

##Test Case 1
##>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog2.py ============
##Enter any number : 1056892
##1056892 is even
##
##
##Press the enter key to quit
##
##Test Case 2
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog2.py ============
##Enter any number : 568942
##568942 is even
##
##
##Press the enter key to quit
##
##Test Case 3
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog2.py ============
##Enter any number : 05
##5 is odd
##
##
##Press the enter key to quit


#Claire Rhoda
#1068768
#Program 3
#Program that determines whether the character entered is a vowel or not

#user inputs a character
char = input("Enter any character :")

#processing if is a character is a vowel or not
if (char == 'A' or char ==  'E' or char == 'I' or char == 'O' or char == 'U'):
    print(char,"is a vowel")
elif (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
    print(char,"is a vowel")
else:
    print(char,"is not a vowel")

#ask user to kill program
input('\n\nPress the enter key to quit')

##Test Case 1
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog3.py ============
##Enter any character :I
##I is a vowel
##
##
##Press the enter key to quit
##
##Test Case 2
##>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog3.py ============
##Enter any character :k
##k is not a vowel
##
##
##Press the enter key to quit
##
##Test Case 3
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog3.py ============
##Enter any character :a
##a is a vowel
##
##
##Press the enter key to quit


#Claire Rhoda
#1068768
#Program 4
#Program that determines if the character entered is a upper/lowercase letter or a number

#user inputs a character (either letter or number)
char = input("Enter the character :")

#processes if the character is either an upper/lowercase letter or a number
if (char >= 'A' and char <= 'Z'):
    print("Uppercase character was entered")
elif  (char >= 'a' and char <= 'z'):
    print("Lowercase character was entered")
elif (char >= '0' and char <= '9'):
    print("A number was entered")

#ask user to kill program
input('\n\nPress the enter key to quit')

##Test Case 1
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog4.py ============
##Enter the character :F
##Uppercase character was entered
##
##
##Press the enter key to quit
##
##Test Case 2
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog4.py ============
##Enter the character :2
##A number was entered
##
##
##Press the enter key to quit
##
##Test Case 3
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog4.py ============
##Enter the character :s
##Lowercase character was entered
##
##
##Press the enter key to quit


#Claire Rhoda
#1068768
#Program 5
#Program that prints a number (inputed by user) of horizontal asterisks

#user inputs amount of stars they want
i = int(input("How many stars do you want?"))
while (i <= 20):
    print("*", end = '')
    i = i + 1

#ask user to kill program
input('\n\nPress the enter key to quit')


#Claire Rhoda
#1068768
#Program 6
#This program calculates property tax

#represents the tax factor
TAX_FACTOR = 0.0065

# Get the first lot number.
print('Enter the property lot number or enter -999 to end')
lot = int(input('Enter the lot number: '))

# Continue processing as long as the user does not enter lot number -999.
while lot != -999:
    # Get the property value.
    value = float(input('Enter property value: '))
    # Calculate the property's tax.
    tax = value * TAX_FACTOR
    # Display the tax.
    print('Property tax: $', format(tax, ',.2f'), sep='')
    # Get the next lot number.
    print('Enter the property lot number or enter -999 to end')
    lot = int(input('Enter the lot number: '))


##Test Case 1
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog6.py ============
##Enter the property lot number or enter -999 to end
##Enter the lot number: 500
##Enter property value: 6000.00
##Property tax: $39.00
##Enter the property lot number or enter -999 to end
##Enter the lot number: -999
##
##Test Case 2
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog6.py ============
##Enter the property lot number or enter -999 to end
##Enter the lot number: 598
##Enter property value: 90000.00
##Property tax: $585.00
##Enter the property lot number or enter -999 to end
##Enter the lot number: 785
##Enter property value: 658000.00
##Property tax: $4,277.00
##Enter the property lot number or enter -999 to end
##Enter the lot number: -999
##
##Test Case 3
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog6.py ============
##Enter the property lot number or enter -999 to end
##Enter the lot number: 5689
##Enter property value: 785000.50
##Property tax: $5,102.50
##Enter the property lot number or enter -999 to end
##Enter the lot number: 895
##Enter property value: 5000.00
##Property tax: $32.50
##Enter the property lot number or enter -999 to end
##Enter the lot number: -999


#Claire Rhoda
#1068768
#Program 7
# This program calculates retail prices.
markup = 0.025
another = 'y'or 'Y'
none = 'n'or 'N'
price = float(input("Enter the item’s wholesale cost: "))

while price < 0:
    print("ERROR: the cost cannot be negative")
    price = float(input("Enter the correct wholesale cost: "))

while price >= 0.0:
    retailPrice = (markup *  price)
    print("Retail price is $",format(retailPrice,',.2f'))
    again = input('Do you have another item? (Enter y for yes): ')
    if another == 'y' or another == 'Y':
        price = float(input("Enter the item's wholesale cost: "))
    elif none == 'n' or none == 'N':
        print()


#Claire Rhoda
#1068768
#Program 8
#This program prints a message five times

#for loop working with the range function
for x in range(5):
    print('Barzinger')

#ask user to quit the program
input('\nPress enter to quit')

##Test Case 1
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog8.py ============
##Barzinger
##Barzinger
##Barzinger
##Barzinger
##Barzinger


#Claire Rhoda
#1068768
#Program 9
#This program calculates the sum of a series of numbers entered by the user.

#user inputs number of numbers they want to find the sum of
max = int(input('How many numbers do you want to add?'))

# Initialize an accumulator variable.
total = 0.0

# Get the numbers and accumulate them.
for counter in range(max):
   number = int(input('Enter a number: '))
   total = total + number

# Display the total of the numbers.
print('The total is', total)

#ask user to kill program
input('\n\nPress the enter key to quit')

##Test Case 1
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog9.py ============
##How many numbers do you want to add?4
##Enter a number: 34
##Enter a number: 23
##Enter a number: 566
##Enter a number: 1
##The total is 624.0
##
##
##Press the enter key to quit
##
##Test Case 2
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog9.py ============
##How many numbers do you want to add?-3
##The total is 0.0
##
##
##Press the enter key to quit
##
##Test Case 3
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog9.py ============
##How many numbers do you want to add?3
##Enter a number: -34
##Enter a number: -67
##Enter a number: -22
##The total is -123.0
##
##
##Press the enter key to quit


#Claire Rhoda
#1068768
#Program 10
#This program converts the speeds 60 kph through 130 kph (in 10 kph increments) to mph.
start_speed = 60
end_speed = 131
increment = 10

# Conversion factor
conversion_factor = 0.6214

# Print the table headings.
print('KPH\tMPH')
print('-------------------------')
# Print the speeds.
for kph in range(start_speed, end_speed, increment):
   mph = kph * conversion_factor
   print(kph, '\t', format(mph, '.1f'))

#ask user to kill program
input('\n\nPress the enter key to quit')


##Test Case 1
##>>>
##============ RESTART: /Users/clairerhoda/Documents/lab2_prog10.py ============
##KPH	MPH
##-------------------------
##60 	 37.3
##70 	 43.5
##80 	 49.7
##90 	 55.9
##100 	 62.1
##110 	 68.4
##120 	 74.6
##130 	 80.8
##
##
##Press the enter key to quit
