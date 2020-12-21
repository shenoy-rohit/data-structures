# Time Complexity: O(N), Space Complexity: O(1)
def isMonotonic(array):
    if len(array) <= 2:
        return True

    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            isNonIncreasing = False
        if array[i] < array[i - 1]:
            isNonDecreasing = False

    return isNonIncreasing or isNonDecreasing

def main():
    print(isMonotonic([1, 1, 1, 2, 3, 5, 6, 8, 100]))
    print(isMonotonic([1, -1, 1, 2, 3, 5, 6, 8, 100]))
    print(isMonotonic([-1, -1, -1, -2, -3, -5, -6, -8, -100]))

if __name__=="__main__":main()

