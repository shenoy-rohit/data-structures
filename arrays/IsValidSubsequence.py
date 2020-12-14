'''
Given two non-empty arrays of integers, write a function that determines whether the second array is a sub-sequence of the first.
Subsequence of numbers aren't necessarily adjacent, but occur in the same order as the original sequence.
'''

# Solution 1 - Space: O(1), Time: O(N^2)
def isValidSubsequence(array, sequence):
    currMatch = -1

    for elem in sequence:
        if elem in array and array.index(elem) >= currMatch:
            currMatch = array.index(elem)
        else:
            return False
    return True

# Solution 2 - Space: O(1), Time O(N)
def isValidSub(array, sequence):

    subSequenceIndex = 0
    mainIndex = 0
    matches = 0

    while mainIndex < len(array) and subSequenceIndex < len(sequence):
        if array[mainIndex] == sequence[subSequenceIndex]:
            subSequenceIndex += 1
            matches += 1
        mainIndex += 1

    return matches == len(sequence)

def main():
    x = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1,6,-1, 10])
    print(x)

    y = isValidSub([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    print(y)

    z = isValidSub([1, 1, 1, 25, 6, 1, 1, 1], [1, 1, 1, 1])
    print(y)

if __name__ == "__main__": main()
