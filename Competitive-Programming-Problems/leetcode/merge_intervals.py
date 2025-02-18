# Summary: Given a set of intervals, merge all overlapping intervals.

# Approach:
#     Sort intervals by start time.
#     Compare the current interval with the previous one and merge if they overlap.

# Complexity:
#     Time: O(n log n) due to sorting
#     Space: O(n)


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
