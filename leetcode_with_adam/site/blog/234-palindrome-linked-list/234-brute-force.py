# brute force O(n^2) solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def get_length(self,head):
        probe = head
        counter = 0
        while probe:
            probe = probe.next
            counter += 1
        return counter

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # edge case when linked list is empty
        if head is None:
            return True

        curr = head
        counter = self.get_length(head)

        for i in range(self.get_length(head)):
            tail = head
            for j in range(counter-1):
                tail = tail.next
            
            if curr.val != tail.val:
                return False
            
            # move to next step
            curr = curr.next
            counter = counter - 1

        
        return True
