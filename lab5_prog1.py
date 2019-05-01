#Claire Rhoda
#106768
#Program 1
#This program prints python statements based on a given dictionary


def allKeys(grade)->None:
    """keys in dict are retrieved"""
    print("\nAll the keys:")  #some prints statements are put before   
    for key in grade.keys():  #loop so the statement is not repeated
        print(key)  #keys are found in dict


def allValues(grade)->None:
    """values in dict are retrieved"""
    print("\nAll the values:")
    for key in grade.keys(): #values are found in dict
        print(grade[key])

    #another way to do it 
    #for val in grade.values():
        #print(val)
    

def pairs(grade)->None:
    """The key and value pairs are retrieved"""
    print("\nThe key and value pairs:")
    for key in grade.keys():  #with one loop, key and values can be
        print(key, grade[key])  #retrieved separatly


def pairOrder(grade)->None:
    """The key and value pairs are sorted in key order"""
    print('\nThe key and pairs in key order:')
    keyList = []  #list is created because dict is immutable
    for key in grade.keys():
        keyList.append(key) #each key is added to new list
    keyList.sort() #key is sorted alphabetically

    for index in keyList:
        #index from keyList and values from grade dict
        print(index, grade[index]) 
       

def avgValue(grade)->None:
    """average of values in dict are retrieved"""
    sum = 0
    for val in grade.values():
        sum += val #sum adds up previous values in list

    avg = sum / 2 
    print('\nThe average value:',avg)


def main():
    """grade creates a dict"""
    grade = {"A":8,"D":3,"B":15,"F":2,"C":6}

    #functions are called and given grade
    allKeys(grade)
    allValues(grade)
    pairs(grade)
    pairOrder(grade)
    avgValue(grade)


if __name__ == "__main__":
    main()
