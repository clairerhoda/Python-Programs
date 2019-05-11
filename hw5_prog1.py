#Claire Rhoda
#1068768
#Program 1
#This program organizes a given text file alphabetically into rows and columns

def rowTotal(teaData)->dict:
    teaDict = {}
    teaLines = teaData.split('\n')
    for index in teaLines:
       numList = []
       elements = index.split(":")
       sum = 0
       for number in elements[1:]:
           sum += float(number)
           numList.append(float(number))
       numList.append(sum)
       teaDict[elements[0]] = numList
    return teaDict
       
def alphaOrder(teaDict)->dict:
    keyList = []
    for keys in teaDict.keys():
        keyList.append(keys)
        keyList.sort()
        print(keyList)
    for tea in keyList:
        numLine = teaDict[tea]
        print(tea,format(numLine[0],"12"),numLine[1],numLine[2],numLine[3])

    
def columnTotal(teaData)->dict:
    numList = []
    teaLines = teaData.split('\n')
    for index in teaLines:
       elements = index.split(":")
        
           
    
      
    
def main():
    teaTextFile = open('tea.txt','r')
    teaData = teaTextFile.read()

    each_kind = rowTotal(teaData)
    alphaOrder(each_kind)
    all_kinds = columnTotal(teaData)
    teaTextFile.close()

if __name__ == "__main__":
    main()
