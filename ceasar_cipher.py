"""
Write a complete console program that implements a Caesar cipher or rotation cipher
, which is a crude system of encoding strings by shifting every letter forward by a given number. 
Your program should prompt the user to type a message and an encoding "key" (number of places to shift each character) and 
display the shifted message. For example, if the shift amount is 3, then the letter A becomes D, and B becomes E, and so on. 
Letters near the end of the alphabet wrap around for a shift of 3, X becomes A, and Y becomes B, and Z becomes C. 
Here are two example dialogues:

    Your message? Attack zerg at dawn
    Encoding key? 3
    DWWDFN CHUJ DW GDZQ

    Your message? DWWDFN CHUJ DW GDZQ
    Encoding key? -3
    ATTACK ZERG AT DAWN

"""
import string

string.ascii_letters
def ceasar_cipher():
    encNum = int(input("Enconding Key? "))
    msg = input("Mesajınızı girin. ") 
    for i in msg:
        if(i != " "):
            print(string.ascii_letters[string.ascii_letters.index(i)+encNum].upper(), end="")
        else:
            print(" ", end="")

ceasar_cipher()
