# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # edge case, empty linkedlist [], so none
        if head is None:
            return False
        
        # set up two pointers
        slow = head
        fast = head


        while fast.next and fast.next.next:
            # fast advances two steps while slow advances one step
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        # if it reaches here, linked list has an end node, null
        return False