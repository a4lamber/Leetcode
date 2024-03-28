# 这题完全可以用25题一样的模版

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head

        dummy = ListNode(None,head)
        ll_length = 0
        curr = head
        while curr:
            ll_length += 1
            curr = curr.next
        
        number_of_groups = ll_length//2

        curr = head
        starting_node = head
        last_group_tail_node = dummy
        
        for _ in range(number_of_groups):
            prev = None
            # reverse
            for i in range(2):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # reconnect
            last_group_tail_node.next = prev
            last_group_tail_node = starting_node
            starting_node.next = curr
            starting_node = curr
        
        return dummy.next





        

