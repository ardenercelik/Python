# Write a function named add_commas that accepts a string 
# representing a number and returns a new string with a comma 
# at every third position, starting from the right. For example, 
# the call of add_commas("12345678") returns "12,345,678".

import math

def add_commas(number):
    number = str(number)
    
    lenN = len(number)
    if lenN <= 3 : 
        print(number)
        return

    x = math.floor(lenN/3)
    listNum = list(number)
    j = len(number)
    for i in range(x):
        listNum.insert( j - 3 , ",")
        j -= 3
        
    print("".join(listNum))

add_commas(2115165)
add_commas(234)
add_commas(2)
add_commas(99999999)

    
    



        


    

