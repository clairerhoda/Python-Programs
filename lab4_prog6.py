#Claire Rhoda
#1068768
#Program 6
#This program tests if the two words entered by a user is an anagram.


def are_anagrams(word1,word2)->None:
    listWord1 = []
    listWord2 = []
    for letters in word1:
        listWord1.append(letters)
        listWord1.sort()
    for letters1 in word2:
        listWord2.append(letters1)
        listWord2.sort()
    if listWord1 == listWord2:
        print("The words",word1,"and",word2,"are anangrams.")
    else:
        print("The words",word1,"and",word2,"are not anangrams.")


def main():
    try:
        two_words = input("Enter two space separated words:")
        word1,word2 = two_words.split() #splits the string
        are_anagrams(word1,word2)

    except ValueError:
        print("Bad Input")

if __name__ == "__main__":
    main()

# Test Case 1
# >>>
# =============== RESTART: /Users/clairerhoda/Documents/test.py ===============
# Enter two space separated words:listen silent
# The words listen and silent are anangrams.

# Test Case 2
# >>>
# =============== RESTART: /Users/clairerhoda/Documents/test.py ===============
# Enter two space separated words:good dog god
# Bad Input

# Test Case 3
# >>>
# =============== RESTART: /Users/clairerhoda/Documents/test.py ===============
# Enter two space separated words:wrong
# Bad Input

# Test Case 4
# >>>
# =============== RESTART: /Users/clairerhoda/Documents/test.py ===============
# Enter two space separated words:fred
# Bad Input

# Test Case 5
# >>>
# =============== RESTART: /Users/clairerhoda/Documents/test.py ===============
# Enter two space separated words:fred joe mary
# Bad Input

# Test Case 6
# >>>
# =============== RESTART: /Users/clairerhoda/Documents/test.py ===============
# Enter two space separated words:cinema iceman
# The words cinema and iceman are anangrams.
# >>>