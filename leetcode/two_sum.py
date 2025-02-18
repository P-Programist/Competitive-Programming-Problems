# Summary: Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.

# Approach:
#     Use a hash map (dictionary in Python) to store num -> index.
#     For each number, check if target - num is in the dictionary. If yes, you found a pair.

# Complexity:
#     Time: O(n)
#     Space: O(n)

def twoSum(nums, target):
    lookup = {}
    for i, val in enumerate(nums):
        complement = target - val
        if complement in lookup:
            return [lookup[complement], i]
        lookup[val] = i
    return []
