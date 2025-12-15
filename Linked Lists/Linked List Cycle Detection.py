# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head and head.next != None:
            if head.next in visited:
                return True
            visited.add(head.next)
            head = head.next

        return False