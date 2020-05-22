"""
index 01234567890123456789012
     "GGGA-GAATCTCTGGACT"
     "CTCTACTTA-AGACCGGTACAGG"

"""
dna1 = "GGGA-GAATCTCTGGACT"
dna2 ="CTCTACTTA-AGACCGGTACAGG"

def dna_errors(dna1, dna2):
    myList = []
    myList.append(dna1)
    myList.append(dna2)
    minD = len(min(myList, key=len))
    maxD = len(max(myList, key=len))
    errCounter = 0
    errCounter = maxD - minD + errCounter
    if len(dna1) != len(dna2):
        dna1 = min(myList, key=len).upper()
        dna2 = max(myList, key=len).upper()
    for i in range(minD):
        if dna1[i] == "-":
            errCounter = errCounter + 1
            continue
        if dna2[i] == "-":
            errCounter = errCounter + 1
            continue
        if dna1[i] == "G" and dna2[i] != "C":
            errCounter = errCounter + 2
        if dna1[i] == "C" and dna2[i] != "G":
            errCounter = errCounter + 2
        if dna1[i] == "A" and dna2[i] != "T":
            errCounter = errCounter + 2
        if dna1[i] == "T" and dna2[i] != "A":
            errCounter = errCounter + 2
    print(errCounter)



dna_errors(dna1, dna2)