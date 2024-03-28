# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # range of k is fairly large, need to calculate the lenght of linked list and modulus it.
        if k == 0 or head is None: return head
        

        # n the length of linked list
        n = 0
        dummy = ListNode(None,head)
        tail, curr = dummy, head
        while curr:
            n += 1
            curr = curr.next
            tail = tail.next

        if k%n == 0: return head
        
        # update k
        k = k%n

        prev,curr = dummy, head
        
        for i in range(n - k):
            prev = prev.next
            curr = curr.next
        
        prev.next = None
        dummy.next = curr
        tail.next = head
    
        return dummy.next

        
        

        
