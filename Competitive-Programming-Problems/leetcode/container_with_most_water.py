# Summary: Given n lines, choose two different lines so that the container can store the most water.

# Approach:
#     Two-pointer approach starting at left = 0, right = n-1. Move the pointer that has the smaller height inwards.

# Complexity:
#     Time: O(n)
#     Space: O(1)


def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water