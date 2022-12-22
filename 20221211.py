# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

def wordDistance(firstInput,secondInput):
    
    differNumber = 0
    differLetter = []

    if ( len(firstInput) >  len(secondInput)) : 
        shorterInput = secondInput
        longerInput = firstInput
    else :
        shorterInput = firstInput
        longerInput = secondInput
    
    for index in range(len(shorterInput)) :
        tempDif = []
        if( firstInput[index] != secondInput[index]): 
            tempDif.append(firstInput[index])
            tempDif.append(secondInput[index])
            differLetter.append(tempDif)
            differNumber += 1

    for index in range ( len(shorterInput)-1 , len(longerInput)-1 ) :
        differLetter.append(longerInput[index])
        differNumber += 1
    return differNumber,differLetter

print("<\tWordDistance\t>")
firstInput = input("\n\nFirst word : ") 
secondInput = input("\nSecond word : ")
print("--------------------------------------------")
print("\nnumber of difference letter(s) : ",wordDistance(firstInput, secondInput)[0])
print("\nhow letter(s) differ : ",wordDistance(firstInput, secondInput)[1],"\n")