# Summary: Return an array answer such that answer[i] is the product of all elements of nums except nums[i].

# Approach:
#     Two-pass strategy (or prefix/suffix).
#     left[i] = product of all elements to the left.
#     right[i] = product of all to the right.
#     res[i] = left[i] * right[i].

# Complexity:
#     Time: O(n)
#     Space: O(1) (not counting output array)


def productExceptSelf(nums):
    n = len(nums)
    res = [1]*n
    
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    
    return res
