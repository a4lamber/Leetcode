# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # three pointer technique, 在swap的时候，需要第三个pointer

        # check for edge cases
        if head is None or head.next is None:
            return head
        
        # set up a dummy node 
        dummy = ListNode(None)
        dummy.next = head

        # initialze three nodes
        prev = dummy
        
        while head and head.next:
            # advanced left and right node from the
            left = head
            right = head.next

            # swap nodes and rejoin
            left.next = right.next
            right.next = left
            prev.next = right

            # update the prev and head node for the next time step
            prev = left
            head = prev.next
            
            
            # update head to the new position
        return dummy.next
w