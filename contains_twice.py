"""
Write a function named contains_twice that accepts a string and a 
character as parameters and returns True if that character occurs two or more 
times in the string. For example, the call of contains_twice("hello", 'l') should 
return True because there are two 'l' characters in that string. 

"""



def contains_twice(word, letter):
    letterIndex = word.find(letter)
    if letterIndex != -1:
        wordList = list(word)
        wordList.remove(wordList[letterIndex])
        if letter in wordList:
            return True
    else:
        return False

print(contains_twice("hello", "l"))
print(contains_twice("yunus", "l"))
print(contains_twice("y", "l"))
print(contains_twice("ll", "l"))

