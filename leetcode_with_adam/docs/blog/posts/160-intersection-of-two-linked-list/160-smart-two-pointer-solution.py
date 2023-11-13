# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        probeA = headA
        probeB = headB

        while probeA != probeB:
            if probeA is None:
                probeA = headB
            else:
                probeA = probeA.next
            
            if probeB is None:
                probeB = headA
            else:
                probeB = probeB.next

        # if no intersection, both probe points to null
        # if intersect, both at same place
        return probeA
            
            