# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

def strToListFloat(inputList) : 
    tempList = inputList.split()
    ListInt = [] 
    for i in range(len(tempList)) : 
        temp = int(tempList[i])
        ListInt.append(temp)
    return ListInt

def findMedian(list):
    resultList = []  
    # size of sublist 
    for i in range (1,len(list)+1):     
        if( i == 1 ) : 
            resultList.append(list[i-1])
        elif( i % 2 == 0): 
            median = (list[int((i/2)-1)] + list[int((i/2))] )/2
            resultList.append(median)
        elif( i % 2 != 0): 
            median = list[int(i/2)]
            resultList.append(median)
    return resultList
    
def adjustList(list): 
    resultList = []
    for i in range (1,len(list)+1):
        lesserList = []
        for j in range (i) : 
            lesserList.append(list[j])
        resultList.append(lesserList)
    return resultList

inputList = input( "Enter List : ")
cleanInput = inputList.replace(","," ")
algoList = strToListFloat(cleanInput)
algoList = sorted(algoList)
resultList = findMedian(algoList)
adjustListResult = adjustList(algoList)

print((adjustListResult))
print((resultList))

