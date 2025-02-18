# Summary: Given a string s, return the longest palindromic substring.

# Approach:
#     Expand around center for each index (both odd and even length palindromes).
#     Keep track of the maximum length found.

# Complexity:
#     Time: O(n^2)
#     Space: O(1)


def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # Odd length
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(res):
                res = s[left:right+1]
            left -= 1
            right += 1

        # Even length
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(res):
                res = s[left:right+1]
            left -= 1
            right += 1

    return res
