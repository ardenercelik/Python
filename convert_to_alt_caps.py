"""
Write a function named convert_to_alt_caps that accepts a string as a parameter and returns a version of the 
string where alternating letters are uppercase and lowercase, starting with the first letter in lowercase. 
For example, the call of convert_to_alt_caps("Pikachu") should return "pIkAcHu". 

"""

def convert_to_alt_caps(word):
    wordList = list(word)
    for i in range(len(word)):
        if i % 2 == 0:
            wordList[i] = wordList[i].lower()
        else:
           wordList[i] = wordList[i].upper() 
    print("".join(wordList))


# convert_to_alt_caps("Pikacu")
# convert_to_alt_caps("arden")
# convert_to_alt_caps("isbank")


"""
Write a function named count_words that accepts a string as 
its parameter and returns the number of words in it. A word is a 
sequence of one or more non-space characters. For example, the call of 
count_words("What is your name?") should return 4. 

"""

def count_words(sentence):
    sList = sentence.split()
    print("There are {} words in this sentence.".format(len(sList) ) )


count_words("What is your name?")




    
    
