from itertools import groupby

def name_diamond(name):
    name = name.upper()
    for i in range(len(name)):
        print(name[:i+1])
    for i in range(len(name)):
        print( " "*(i+1) + name[i+1:])
name_diamond("arden")

# sentencedan letter harflerini çıkar
def remove_all(sentence, letter):
    listSentence = list(sentence)
    while letter in listSentence:
        listSentence.remove(letter)
    print("".join(listSentence))
#remove_all("Summer is here!", 'e')

def remove_duplicates(sentence):
    listSentence = list(sentence)
    for i in range(len(listSentence)):
        if i == len(listSentence) - 1:
            break
        try:
            while listSentence[i] == listSentence[i+1]:
                listSentence.remove(listSentence[i])
        except:
            pass
    print("".join(listSentence))

    
remove_duplicates("bookkeeeeeper")
remove_duplicates("mpptt")
remove_duplicates("rrrrrrrr")
remove_duplicates("a")
remove_duplicates("arden")