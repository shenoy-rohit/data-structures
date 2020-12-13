'''
Write a function that takes a non-empty array of distinct integers, and an integer representing a target sum.
If any two numbers in the array sum upto the target sum, return the two numbers
Else, return an empty array.
'''

# Prompt:
    # Distinct & non-empty integer array
    # Returns two integers - any order
    # Return empty ARRAY else
    # No doubling;
    # At most one pair of numbers summing up to target only

def twoNumberSum(array, targetSum):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    else:
        return []

def twoNumSumHash(array, targetSum):

    # create hash table
    myHashTable = {}

    for i in range(0, len(array)):
        if targetSum - array[i] in myHashTable:
            return [array[i], targetSum - array[i]]
        else:
            myHashTable[array[i]] = True
    return []

def twoNumSumLeftRight(array, targetSum):
    array.sort()

    leftPointer = 0
    rightPointer = len(array) - 1

    while leftPointer < rightPointer:
        if array[leftPointer] + array[rightPointer] > targetSum:
            rightPointer -=1
        elif array[leftPointer] + array[rightPointer] < targetSum:
            leftPointer +=1
        else:
            return [array[leftPointer], array[rightPointer]]
    return []

def main():
    # Time Complexity - O(N^2), Space complexity - O(1)
    x = twoNumberSum([1, 4, -3, 5, 7], 9)
    print(x)

    # Time Complexity - O(N), Space complexity - O(N)
    y = twoNumSumHash([1, 4, -3, 5, 7], 9)
    print(y)

    # Time Complexity - O(N logN), Space complexity - O(1)
    z = twoNumSumLeftRight([3, 5, -1, -2, 7, 4, 10], 9)
    print(z)

if __name__== "__main__": main()