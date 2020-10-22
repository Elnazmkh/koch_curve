def palindrome_check(str1):
    """
    Checks if a given word is a palinndrome.

    Parameters :
    str1 (str) : a word

    Returns :
    True (bol): if the word is a palindrome.
    False (bol) : if the word is NOT a palindrome.
    """
    str1 = str1.lower()
    if str1[0] != str1[-1]:
        return False
    elif len(str1) < 4 and str1[0] == str1[-1]:
        return True
    else:
        return palindrome_check(str1[1:-1])


# --------------------------------------------------------

word = input("Enter the word to check: ")

if palindrome_check(word):
    print("Palindrome!")
else:
    print("Not Palindrome!")