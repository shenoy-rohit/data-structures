# Time Complexity = O(NlogN + MlogM)
# Space Complexity = O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    smallestDiff = float("inf")
    leftInd = 0
    rightInd = 0
    answer = []

    while leftInd < len(arrayOne) and rightInd < len(arrayTwo):
        firstNum = arrayOne[leftInd]
        secondNum = arrayTwo[rightInd]

        if firstNum == secondNum:
            return [firstNum, secondNum]

        currentDiff = abs(firstNum - secondNum)
        if firstNum < secondNum:
            leftInd += 1
        elif firstNum > secondNum:
            rightInd += 1

        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
            answer = [firstNum, secondNum]
    return answer

def main():
    x = smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17])
    print(x)

if __name__ == '__main__':main()
