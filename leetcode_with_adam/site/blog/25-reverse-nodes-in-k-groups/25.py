# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # step1: traver to get the length
        dummy = ListNode(None,head)
        
        ll_length = 0
        
        curr = head
        while curr:
            ll_length += 1
            curr = curr.next
        # step2: compute necessary infos
        num_of_groups = ll_length//k
        num_of_left_out_nodes = ll_length%k

        # step3:         
        curr = head
        last_group_tail_node = dummy 
        start_node = head
        for _ in range(num_of_groups):
            prev = None
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            last_group_tail_node.next = prev
            last_group_tail_node = start_node
            start_node.next = curr
            start_node = curr
            
            

        return dummy.next

