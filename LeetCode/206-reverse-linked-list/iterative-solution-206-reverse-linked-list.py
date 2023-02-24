# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iteratative sotluon
        # set up two pointer
        prev = None
        curr = head

        while curr:
            # assuming curr at node[i], prev at node[i-1], index convention是根据old linked list

            # construct a temo points to node[i+1]
            temp = curr.next
            # points node[i] to node[i-1]
            curr.next = prev
            # update prev from node[i-1] to node[i]
            prev = curr
            # update curr pointer to node[i+1] (for the old linked list)
            curr = temp
        
        # iteration结束时, curr在null, prev是new head of the linked list
        return prev
