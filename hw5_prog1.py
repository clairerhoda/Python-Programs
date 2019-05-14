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
    for tea in keyList:
        numLine = teaDict[tea]
        print(tea,format(numLine[0],"12.2f"),format(numLine[1],"12.2f"),\
              format(numLine[2],"12.2f"),format(numLine[3],"12.2f"))

def columnTotal(teaDict)->str:
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for value in teaDict.values():
        sum1 += value[0]
        sum2 += value[1]
        sum3 += value[2]
    print(format(sum1,'21.2f'),format(sum2,'12.2f'),format(sum3,'12.2f'))
    
def main():
    teaTextFile = open('tea.txt','r')
    teaData = teaTextFile.read()

    each_kind = rowTotal(teaData)
    alphaOrder(each_kind)
    all_kinds = columnTotal(each_kind)
    teaTextFile.close()

if __name__ == "__main__":
    main()
