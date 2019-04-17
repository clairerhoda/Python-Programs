def main():
    numbers = makeList()
    odd = delEven(numbers)
    print("Original List-",numbers)
    print("List after deleting even numbers:",odd)

def delEven(numbers:list)->list:
    odd = []
    for even in numbers:
        if numbers[even] % 2 != 0: 
            odd.append(even)
    return odd

def makeList()->list:
    numbers = list(range(1,11))
    return numbers

if __name__ == "__main__":
    main()
