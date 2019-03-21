#Claire Rhoda
#1068768
#Program 5
#This program gets the first, middle, and last name of a person and
#displays their initials

def fullname()->(str):
    user_input = input("Enter yout full name")
    return (user_input)

def separate(firstMiddleLast:str)->(str,str,str):
    sections = firstMiddleLast.split(' ')
    first = sections[0]
    middle = sections[1]
    last = sections[2]
    return (first,middle,last)

def getInitials(first:str,middle:str,last:str)->str:
    l1 = first[0:1]
    l2 = middle[0:1]
    l3 = last[0:1]
    Initials = (l1 +"." + l2 + "." + l3 + ".")
    return Initials

def main():
    firstMiddleLast = fullname()
    first,middle,last = separate(firstMiddleLast)
    initials = getInitials(first,middle,last)
    print(initials)

if __name__ == "__main__":
    main()
    
    
    
    

