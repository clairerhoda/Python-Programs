#Claire Rhoda
#1068768
#Program 2
#This program translates the user inputed abbreviation to English

def abbvDict(abbvData:str)->dict:
    abbvDictionary = {}
    abbvLines = abbvData.split('\n')
    for index in (abbvLines):
        key_value = index.split(':')
        abbvDictionary[key_value[0]] = key_value[1]
    return abbvDictionary


def transaltedAbbv(abbv:dict,makeDict:dict)->str:
    return makeDict[abbv]

def main():
    abbvTextFile = open('textabbv.txt' ,'r')
    abbvData = abbvTextFile.read()

    makeDict = abbvDict(abbvData)
    print(makeDict)
    abbv = input("Enter a message to be translated:\n")
    newList = []
    newList.append(abbv.lower())
    print("The translated text is:\n",transaltedAbbv(abbv,makeDict))

if __name__ == "__main__":
    main()
