#Claire Rhoda
#1068768
#Program 1
#This program organizes a given text file alphabetically into rows and columns

def columnTotal(teaData)->dict:
    teaLines = teaData.split('\n')
    for index in teaLines:
       numList = []
       elements = index.split(":")
       sum = 0
       for number in elements[1:]:
           sum += float(number)
           numList.append(float(number))
       numList.append(sum)
       teaDict = {elements[0]: numList}
       

def rowTotal(teaData)->dict:
    twoDim = []
    teaLines = teaData.split('\n')
    for index in teaLines:
       elements = index.split(":")
       numList = []
       
       for number in elements[1:]:
          numList.append(number)
    
       twoDim.append(numList)
    sum = 0
    column = 0
    row = 0
    for i in twoDim[column]:
        for num in twoDim[row]:
            sum += float(i)
            column += 1
            row += 1
            print(sum)
       
        
def main():
    teaTextFile = open('tea.txt','r')
    teaData = teaTextFile.read()

    each_kind = columnTotal(teaData)
    all_kinds = rowTotal(teaData)
    teaTextFile.close()

if __name__ == "__main__":
    main()
