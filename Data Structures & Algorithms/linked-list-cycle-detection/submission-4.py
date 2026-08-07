# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s, f = head, head.next
        while s and f:
            if f == s:
                return True
            if f.next:
                f = f.next.next
            else:
                break
            s = s.next
        return False