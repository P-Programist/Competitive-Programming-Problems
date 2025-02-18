# Summary: Find the contiguous subarray within an integer array that has the largest sum.

# Approach (Kadane’s Algorithm):
#     Keep track of the current sum. If it drops below 0, reset it.
#     Track the max sum at each iteration.

# Complexity:
#     Time: O(n)
#     Space: O(1)


def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
