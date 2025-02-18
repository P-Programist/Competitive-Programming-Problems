# Summary: Given an array of distinct integers and a target, find all unique combinations of candidates where the chosen numbers sum to the target (unlimited use of each candidate).

# Approach:
#     Backtracking. At each step, either use the current candidate if it doesn’t exceed the target or skip to the next candidate.

# Complexity:
#     Time: O(n^(target/min_candidate)) in the worst case
#     Space: O(target/min_candidate)


def combinationSum(candidates, target):
    res = []
    candidates.sort()

    def backtrack(start, cur_sum, path):
        if cur_sum == target:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            if cur_sum + num > target:
                break
            backtrack(i, cur_sum + num, path + [num])
    
    backtrack(0, 0, [])
    return res