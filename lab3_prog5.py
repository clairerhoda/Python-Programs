#Claire Rhoda
#1068768
#Program 5
#This program takes the inputed first, middle, and last name of a person and
#displays their initials

def separate(user_input:str)->(str,str,str):
    sections = user_input.split( )
    for name in sections:
        first,middle,last = name[0]
        return(first,middle,last)
   


def getInitials(first:str,middle:str,last:str)->str:
    l1 = first[0:1]
    l2 = middle[0:1]
    l3 = last[0:1]
    Initials = (l1 +"." + l2 + "." + l3 + ".")
    return Initials


def main():
    user_input = input("Enter yout full name")
    first,middle,last = separate(user_input)
    initials = getInitials(first,middle,last)
    print(initials)


if __name__ == "__main__":
    main()
    
    
    
    

