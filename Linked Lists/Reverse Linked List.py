# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Idea: if empty, return empty
        # If singleton, return singleton
        if head == None or head.next == None:
            return head
        # Three pointers? One ahead of other, point curr2.next to curr1, curr1 = curr2, curr2 = temp, while temp != None
        curr1 = head
        curr2 = curr1.next
        temp = curr2.next
        #logic
        curr2.next = curr1
        curr1.next = None

        while temp:
            curr1 = curr2
            curr2 = temp
            temp = temp.next
            curr2.next = curr1


        return curr2

        