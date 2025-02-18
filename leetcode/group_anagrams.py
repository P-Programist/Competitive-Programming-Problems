# Summary: Group strings that are anagrams of each other.

# Approach:
#     Use a dictionary with a sorted string as the key and the list of anagrams as the value.

# Complexity:
#     Time: O(n * k log k) where n is the number of strings and k is the max length of a string (due to sorting each string).
#     Space: O(nk)


def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        anagrams.setdefault(key, []).append(s)
    return list(anagrams.values())
