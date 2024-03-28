# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> 
Optional[ListNode]:
        # reverse a linked list 三部曲
        # 1. traverse to the left ListNode
        # 2. reverse the linked list portition from left to right
        # 3. reorganize where it points to

        dummy = ListNode(0,head)

        # step 1: traverse to the left ListNode
        prevLeft, curr = dummy,head
        for i in range(left - 1):
            # advancing both pointers
            prevLeft, curr = prevLeft.next, curr.next
        
        # prevLeft: sitting at node before left node
        # curr: sitting at left node
        # step 2: let's reverse until the right ListNode
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # step 3: reorganize the "reversed" linked list
        prevLeft.next.next = curr
        prevLeft.next = prev

        return dummy.next
        

