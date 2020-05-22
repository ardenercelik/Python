"""
 Write a function named is_palindrome that accepts a string 
 parameter and returns True if that string is a palindrome, or False if it is not a palindrome. 
 "dog god" "123 $$ 321""Madam""RACEcar"
 """

def is_palindrome(word):
    if len(word) == 1:
        return False
    reverseWord=""
    for i in range(len(word)):
        x = word[-i-1]
                
        reverseWord = reverseWord + (x)
    if reverseWord.lower() == word.lower():
        return True
    return False

print(is_palindrome("tattarrattat"))

