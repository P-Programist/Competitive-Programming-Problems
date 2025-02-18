# Summary: Merge two sorted linked lists into one sorted list.

# Approach:
#     Maintain a dummy head pointer and a current pointer. Compare the heads of both lists and attach the smaller node to current, then advance pointers accordingly.

# Complexity:
#     Time: O(m + n) (m and n are the lengths of the two lists)
#     Space: O(1) (not counting the output list)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach any remaining nodes
    current.next = l1 if l1 else l2
    return dummy.next
