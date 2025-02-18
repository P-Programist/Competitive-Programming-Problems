# Summary: Check if a string containing characters '(', ')', '{', '}', '[', and ']' is valid. A valid string requires every opening bracket to have a corresponding closing bracket in the correct order.

# Approach:
#     Use a stack. Push opening brackets onto the stack.
#     When you see a closing bracket, pop from the stack and check if it matches.

# Complexity:
#     Time: O(n)
#     Space: O(n)


def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0
