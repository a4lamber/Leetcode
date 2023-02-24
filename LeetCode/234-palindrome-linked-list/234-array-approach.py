
a =  [1,2,3]
a = [1,2,1]

if a == a[::-1]:
    print("h")# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # edge case when linked list is empty
        if head is None:
            return True

        # result list
        res = []

        # set a pointer, so we don't mess up the linkedlist
        probe = head

        # traverse the linked list and append it's value to array
        # O(n), 但是append opeartion on array would be costly and depends on how they 扩容
        while probe:
            res.append(probe.val)
            probe = probe.next
        
        # compare whether array and reverse of the array are equal, O(n) cost
        return res == res[::-1]






