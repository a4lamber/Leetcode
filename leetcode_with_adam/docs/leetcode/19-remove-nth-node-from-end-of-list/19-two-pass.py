# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # travest 1st time and measure the length
        counter = 1
        curr = head
        
        while curr:
            counter += 1    
            curr = curr.next

        # traverse 2nd time and delete
        dummy = ListNode(None,head)
        prev, curr = dummy, head
        while curr:
            counter -= 1
            if counter == n:
                prev.next = curr.next
                break
            
            prev = prev.next
            curr = curr.next
        
        return dummy.next
