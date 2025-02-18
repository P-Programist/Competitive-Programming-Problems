# Summary: Given n, generate all valid combinations of n pairs of parentheses.

# Approach:
#     Backtracking. Keep track of how many left and right parentheses you can still place. Only place a right parenthesis if it doesn’t break validity.

# Complexity:
#     Time: O(Catalan(n)) which is roughly O((4^n)/(n^(3/2)))
#     Space: O(n) for recursion


def generateParenthesis(n):
    res = []

    def backtrack(cur, open_count, close_count):
        if len(cur) == 2*n:
            res.append(cur)
            return
        if open_count < n:
            backtrack(cur + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(cur + ')', open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return res
