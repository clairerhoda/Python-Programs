#Claire Rhoda
#1068768
#Program 1 
#user inputs an age
age = int(input(“Enter the age : ”))
#process for determining the years until eligible to vote if younger than 18
yrs = 18 – age
#processing/output for determining if the age is younger than 18
if (age >= 18):
print(“You are eligible to vote”)
Else:
print(“You have to wait for another “ +yrs +” years to cast your vote”) 

#Claire Rhoda
#1068768
#Program 2
#user inputs any number
num = int(input(“Enter any number : ”))
#processing for even numbers
if (num % 2 == 0):
print(num,”is even”)
#processing for odd numbers
Else:
print(num,“is odd”)
3.
#Claire Rhoda
#1068768
#Program 3
#user inputs a character
char = input(“Enter any character :”)
#processing if is a character is a vowel or not
if (char == ‘A’ or char ==  ‘E or char == ‘I’ or char == ‘O’ or char == ‘U’):
print(char,“is a vowel”)
elif (char == ‘a’ or char == ‘e’ or char == ‘i’ or char == ‘o’ or char == ‘u’):
print(char,“is a vowel”)
Else:
print(ch,“is not a vowel”)

#Claire Rhoda
#1068768
#Program 4
#user inputs a character (either letter or number)
char = input(“Enter the character :”)
#processes if the character is either an upper/lowercase letter or a number
if (char >= “A” and char <= “Z”):
print(“Uppercase character was entered”)
elif  (char >= “a” and char <= “z”):
print(“Lowercase character was entered”)
elif (char >= “0” and char <= “9”):
print(“A number was entered”)

#Claire Rhoda
#1068768
#Program 5
i = 1
#user inputs amount of stars they want
i = int(input(“How many stars do you want?”))
while (i <= 20):
print(“*”, end=“”)
i = i + 1

#Claire Rhoda
#1068768
#Program 6
# This program displays property taxes.
TAX_FACTOR = 0.0065   # Represents the tax factor.
# Get the first lot number.
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))
# Continue processing as long as the user
# does not enter lot number 0.
while lot != 0:
   # Get the property value.
   value = float(input('Enter the property value: '))
   # Calculate the property's tax.
   tax = value * TAX_FACTOR
   # Display the tax.
   print('Property tax: $', format(tax, ',.2f'), sep='')
   # Get the next lot number.
   print('Enter the next lot number or')
   print('enter 0 to end.')
   lot = int(input('Lot number: '))

#Claire Rhoda
#1068768
#Program 7
# This program calculates retail prices.
markup = 0.025
price = float(input(“Enter the item’s wholesale cost: “))
While price < 0:
	print(“ERROR: the cost cannot be negative”)
price = float(input(“Enter the correct wholesale cost: ”)) 
while price >= 0.0:
	retailPrice = (markup *  price)
	print(“Retail price is $”,format(retailPrice,’,.2f’))
	again = input('Do you have another item? ' + \
                   '(Enter y for yes): ')


#Claire Rhoda
#1068768
#Program 8
# This program prints a message five times
for x in range(5):
print('Barzinger')

#Claire Rhoda
#1068768
#Program 9
# This program calculates the sum of a series of numbers entered by the user.
#user inputs number of numbers they want to find the sum of
max = int(input(“How many numbers do you want to add?”))
# Initialize an accumulator variable.
total = 0.0
# Get the numbers and accumulate them.
for counter in range(max):
   number = int(input('Enter a number: '))
   total = total + number
# Display the total of the numbers.
print('The total is', total)

#Claire Rhoda
#1068768
#Program 10
# This program converts the speeds 60 kph through 130 kph (in 10 kph increments) to mph.
start_speed = 60            
end_speed = 131             
increment = 10             
conversion_factor = 0.6214  # Conversion factor
# Print the table headings.
print('KPH\tMPH')
print('-------------------------')
# Print the speeds.
for kph in range(start_speed, end_speed, increment):
   mph = kph * conversion_factor
   print(kph, '\t', format(mph, '.1f'))
