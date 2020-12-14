'''
Write a function that takes a non-empty array of distinct integers, and an integer representing a target sum.
If any THREE numbers in the array sum upto the target sum, return the THREE numbers
Else, return an empty array.

All possible triplets should be returned & the triplets should be sorted, within triplets & overall array of triplets should be sorted.
'''

# Prompt:
    # Distinct & non-empty integer array
    # Returns two integers - any order
    # Return empty ARRAY else
    # No doubling;
    # At most one pair of numbers summing up to target only

# Time-O(N^3), Space = O(N)
def threeNumberSum(array, targetSum):
    triplets = []

    for i in range(0, len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if targetSum == array[i] + array[j] + array[k]:
                    trip = [array[i], array[j], array[k]]
                    trip.sort()
                    triplets.append(trip)
    triplets.sort()
    return triplets

# Time Complexity: O(N^2), Space Complexity: O(N)
def threeNumberSumBetter(array, targetSum):
    array.sort()
    triplets = []

    for ind in range(len(array) - 2):
        left = ind + 1
        right = len(array) - 1

        while left < right:
            currentSum = array[ind] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[ind], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets


def main():
    # Time Complexity - O(N^2), Space complexity - O(1)
    x = threeNumberSum([1, 4, -3, 5, 7], 9)
    print(x)

    # Time Complexity - O(N), Space complexity - O(N)
    y = threeNumberSum([1, 4, -3, 5, 7], 9)
    print(y)

    # Time Complexity - O(N logN), Space complexity - O(1)
    z = threeNumberSumBetter([3, 5, -1, -2, 7, 4, 10], 9)
    print(z)

if __name__== "__main__": main()