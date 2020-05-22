"""
Write a function named is_rotation that accepts two strings as parameters and returns true if they are rotations of each other. 
Two strings are considered rotations if they contain the same characters in the same relative order when wrapped around. 
For example, the call of is_rotation("abcde", "deabc") should return True. 
The call of is_rotation("abcde", "edcba") should return False because the characters are not in the same order. 
A string is also considered to be its own rotation

"""

def is_rotation():
    x = "JavaProgrammer"
    x = x + x

    if x.find("ProgrammerJava") != -1:
        print("true")

def last_first():
    name="Arden Ercelik"
    listName = name.split()
    print("{} {}.".format(listName[1], listName[0][:1]))

last_first()