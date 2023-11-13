# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # step1: find how many pairs of twin nodes
        # step2: sum and find 
        # step3: return miximum twin sum
        # Approach 1: auxillary data structure, array

        # takes O(n) space
        ArrayList = []
        
        # traver the liinked list O(n)
        probe = head
        while probe != None:
            ArrayList.append(probe.val)
            probe = probe.next

        # two pointer
        left,right = 0,len(ArrayList) - 1
        maximumTwinSum = -1

        # traverse half of the list O(n/2) = O(n)
        while left<right:

            if ArrayList[left] + ArrayList[right] > maximumTwinSum:
                maximumTwinSum = ArrayList[left] + ArrayList[right]

            # advances both pointer
            left += 1
            right -= 1
        
        return maximumTwinSum

        
