# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # step1: reverse the 2nd half of the linked list in place (已知)
        #       1.1 find the miidle (two pointer)
        #       1.2 reverse it 
        # step2: traverse and find the sum

 
        # step 1.1
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # step 1.2 now, slow is at the end of 1st half
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            # update pointers
            prev = curr
            curr = temp
        
        # step 2
        first = head
        last = prev
        maxSum = -1
        while last:
            if first.val + last.val > maxSum:
                maxSum = first.val + last.val

            first = first.next
            last = last.next

        return maxSum


