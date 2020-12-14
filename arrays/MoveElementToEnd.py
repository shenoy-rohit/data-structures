# Time Complexity: NLogN
# Space Complexity: O(1)
# Time Complexity: O(N), Space Complexity: O(1)
def moveElementToEnd(array, toMove):
    endIndex = len(array) - 1
    currentInd = 0

    while currentInd < endIndex:
        while array[endIndex] == toMove and currentInd < endIndex:
            endIndex -= 1
        if array[currentInd] == toMove:
            temp = array[endIndex]
            array[endIndex] = array[currentInd]
            array[currentInd] = temp

        currentInd += 1
    return array


# Time Complexity: O(N), Space Complexity: O(1)
def moveElementToEndBetter(array, toMove):
    endIndex = len(array) - 1
    currentInd = 0

    while currentInd < endIndex:
        while array[endIndex] == toMove and currentInd < endIndex:
            endIndex -= 1
        if array[currentInd] == toMove:
            temp = array[endIndex]
            array[endIndex] = array[currentInd]
            array[currentInd] = temp

        currentInd += 1
    return array

def main():
    x = moveElementToEnd([1, 3, 2, 4, 2, 2, 4, 2, 2], 4)
    print(x)

    y = moveElementToEndBetter([1, 3, 2, 4, 2, 2, 4, 2, 2], 2)
    print(y)

if __name__=="__main__":main()