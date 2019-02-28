#intialization
sum = 0
count = 0
#input
num = float(input("Enter a number or -999 to quit"))
while num != -999:
    sum = sum + num
    count = count + 1
    num = float(input("Enter a number or -999 to quit"))

if count != 0:
    avg = sum / count
    print("The sum is",sum)
    print("The average is", avg)
else:
    print("Division by zero error")
