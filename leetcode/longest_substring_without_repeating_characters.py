# Summary: Find the length of the longest substring of a given string that contains no duplicate characters.

# Approach:
#     Use a sliding window and a hash map to track the last index of each character.
#     Move the start of the window forward when a repeat is found.

# Complexity:
#     Time: O(n)
#     Space: O(min(m, n)), where m is the size of the character set and n is the string length


def lengthOfLongestSubstring(s):
    used = {}
    max_len = start = 0

    for i, char in enumerate(s):
        if char in used and used[char] >= start:
            start = used[char] + 1
        used[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len
