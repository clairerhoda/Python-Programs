#Claire Rhoda
#1068768
#Program 6
#This program tests if the two words entered by a user is an anagram.


def are_anagrams(word1,word2)->None:
    """calculates if the two words entered are anagrams"""
    listWord1 = []  #creates lists for letters to be separated
    listWord2 = []
    for letters in word1:
        listWord1.append(letters)
        listWord1.sort()   #sorts the letters in order
    for letters1 in word2:
        listWord2.append(letters1)
        listWord2.sort()  #sort the letters in order
    if listWord1 == listWord2:   #checks if the two lists of letters are equal 
        print("The words",word1,"and",word2,"are anangrams.")
    else:
        print("The words",word1,"and",word2,"are not anangrams.")


def main():
    """tests if input equals two words"""
    try:
        two_words = input("Enter two space separated words:")
        word1,word2 = two_words.split() #splits the string
        are_anagrams(word1,word2)  #calls anagram function and gives words

    except ValueError:
        print("Bad Input")  #if wrong number of words are inputed, error is shown

if __name__ == "__main__":
    main()

input("\nPress Enter to quit")


##Test Case 1
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog6.py ======
##Enter two space separated words:fred
##Bad Input
##
##Press Enter to quit
##
##Test Case 2
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog6.py ======
##Enter two space separated words:fred mary joe
##Bad Input
##
##Press Enter to quit
##
##Test Case 3
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog6.py ======
##Enter two space separated words:cinema iceman
##The words cinema and iceman are anangrams.
##
##Press Enter to quit
##
##Test Case 4
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog6.py ======
##Enter two space separated words:listen silent
##The words listen and silent are anangrams.
##
##Press Enter to quit
##
##Test Case 5
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog6.py ======
##Enter two space separated words:done bun
##The words done and bun are not anangrams.
##
##Press Enter to quit
##
##Test Case 6
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog6.py ======
##Enter two space separated words:anagram margana
##The words anagram and margana are anangrams.
##
##Press Enter to quit
##>>> 
