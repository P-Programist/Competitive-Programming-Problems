# Summary: Given an array of integers, find all unique triplets that sum to zero.

# Approach:
#     Sort the array.
#     Loop over the array, and for each number, use a two-pointer approach to find pairs that make the sum zero.
#     Skip duplicates to avoid repeating the same triplet.

# Complexity:
#     Time: O(n^2)
#     Space: O(1) or O(n) depending on sorting in-place


def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicate
        left, right = i+1, len(nums)-1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return result
