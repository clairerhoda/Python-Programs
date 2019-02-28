start = int(input('Enter start number'))
end = int(input('Enter end number'))
print()
print("Number \t Square")
print('__' * 8)
for number in range(start,end + 1):
    square = number ** 2
    print(number,'\t',square) 
