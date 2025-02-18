# Summary: Two non-empty linked lists representing two non-negative integers (digits in reverse order). Add them and return the sum as a linked list.

# Approach:
#     Traverse both lists simultaneously, summing digits and carrying over as needed.
#     Use a dummy head to build the result list.

# Complexity:
#     Time: O(max(m, n))
#     Space: O(max(m, n))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10

        curr.next = ListNode(total % 10)
        curr = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next
