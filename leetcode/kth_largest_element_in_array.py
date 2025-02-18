# Summary: Find the kth largest element in an unsorted array.

# Approach:
#     Sorting approach is O(n log n).
#     Or use a min-heap of size k or the nth largest selection algorithm (Quickselect) in average O(n).

# Complexity (sorting version):
#     Time: O(n log n)
#     Space: O(1) or O(log n) depending on sorting algorithm


def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]
