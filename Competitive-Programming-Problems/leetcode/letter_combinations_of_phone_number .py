# Summary: Given a string containing digits from 2-9, return all possible letter combinations that the number could represent.

# Approach:
#     Backtracking. Map each digit to possible letters, recurse through each digit building partial solutions.

# Complexity:
#     Time: O(3^n) or O(4^n) depending on the digit distribution
#     Space: O(n) for recursion depth

def letterCombinations(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }
    res = []

    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return
        for char in phone_map[digits[index]]:
            backtrack(index+1, path + char)
    
    backtrack(0, "")
    return res
