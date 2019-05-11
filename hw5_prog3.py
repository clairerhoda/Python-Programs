#Claire Rhoda
#1068768
#Program 2
#This program translates the user inputed abbreviation to English

def transaltedAbbv(abbv:str)->str:
    print(abbvData)

def main():
    abbvTextFile = open('textabbv.txt' ,'r')
    abbvData = abbvTextFile.read()
    print(abbvData)
    abbv = input("Enter a abbreviation to be translated")
    print("The translated text is:\n",transaltedAbbv(abbv))

if __name__ == "__main__":
    main()
