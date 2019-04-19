#Claire Rhoda
#1068768
#Program 7
#This program creates new sets of elements from the three given sets

def aFunc(set1:set,set2:set)->set:
    """elements that are in either set1 or set2"""
    setA = set1^set2  
    return setA


def bFunc(set1:set,set2:set,set3:set)->set:
    """elements that are in only one of the three sets"""
    setB1 = set1^set2
    setB2 = setB1^set3
    return setB2


def cFunc(set1:set,set2:set,set3:set)->set:
    """elements that are in exactly two of the three sets"""
    setC1 = set1&set2
    setC2 = set1&set3
    setC3 = set2&set3  #NO MATCHES BUT CHECKS ANYWAY
    setC4 = setC1|setC2|setC3
    return setC4


def dFunc(set1:set)->set:
    """elements that are in range 1-25 but not in set1"""
    theRange = {1,2,3,4,5,6,7,8,9,10,11,12,13, \
        14,15,16,17,18,19,20,21,22,23,24,25}
    setD = theRange - set1
    return setD


def eFunc(set1:set,set2:set,set3:set)->set:
    """elements that are in range 1-25 but not in any of the three elements"""
    theRange = {1,2,3,4,5,6,7,8,9,10,11,12,13, \
        14,15,16,17,18,19,20,21,22,23,24,25}
    setE1 = theRange - set1
    setE2 = setE1 - set2
    setE3 = setE2 - set3
    return setE3


def fFunc(set1:set,set2:set,set3:set)->set:
    """elements in range 1 to 25 that are not in all three sets"""
    theRange = {1,2,3,4,5,6,7,8,9,10,11,12,13, \
        14,15,16,17,18,19,20,21,22,23,24,25}
    setF1 = set1&set2&set3
    setF2 = theRange - setF1
    return setF2


def main():
    #the main sets used by different functions above
    set1 = {1,2,3,4,5}
    set2 = {2,4,6,8}
    set3 = {1,5,9,13,17} 

    #calls each function for each separate task
    a = aFunc(set1,set2)
    b = bFunc(set1,set2,set3)
    c = cFunc(set1,set2,set3)
    d = dFunc(set1)
    e = eFunc(set1,set2,set3)
    f = fFunc(set1,set2,set3)

   #prints all the returns 
    print("a.",a,sep='')  
    print("b.",b,sep='')
    print("c.",c,sep='')
    print("d.",d,sep='')
    print("e.",e,sep='')
    print("f.",f,sep='')

if __name__ == "__main__":
    main()

input("\nPress Enter to quit")

##Test Case 1
##>>> 
##============ RESTART: /Users/clairerhoda/Documents/lab4_prog7.py ============
##a.{1, 3, 5, 6, 8}
##b.{17, 3, 6, 8, 9, 13}
##c.{1, 2, 4, 5}
##d.{6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
##e.{7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25}
##f.{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
##
##Press Enter to quit
##>>> 
