# Summary: Given a non-empty string s and a dictionary of valid words, determine if s can be segmented into one or more dictionary words.

# Approach:
#     Dynamic programming. dp[i] = true if substring s[:i] can be segmented.
#     For each i, check if there’s a j < i such that dp[j] is true and s[j:i] is in the dictionary.

# Complexity:
#     Time: O(n^2) in worst case
#     Space: O(n)


def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[-1]
