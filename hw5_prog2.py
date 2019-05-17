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


def transaltedAbbv(abbvList:list,makeDict:dict)->str:
    return makeDict[abbvList]
  

def main():
    containsPunc = False
    abbvTextFile = open('textabbv.txt' ,'r')
    abbvData = abbvTextFile.read()
    punc = "!,?,,,-,_,.,{,},[,],(,),&,^,*,%,$,@"
    makeDict = abbvDict(abbvData)
    print(makeDict)
    abbv = input("Enter a message to be translated:\n")
    abbvList = abbv.split(" ")
    for word in abbvList:
        for ch in word[-1]:
            if ch in punc:
                singlePunc = ch
                word = word.strip(ch)
                word = makeDict[word] + ch
            
                print(word,end=' ')
            
            else:
                print(makeDict[word],end=' ')
        

    

if __name__ == "__main__":
    main()
