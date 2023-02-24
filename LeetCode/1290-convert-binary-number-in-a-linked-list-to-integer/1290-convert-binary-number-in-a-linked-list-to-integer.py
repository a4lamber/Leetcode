# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # define a output array
        result = []

        # traverse the linked list
        probe = head
        while probe != None:
            result.append(probe.val)
            probe = probe.next
        
        
        output = 0
        for i in range(len(result)):
            output += 2**(len(result)-i-1) * result[i]

        return output