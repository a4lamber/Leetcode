# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self,head):
        # return the length of the linked list
        probe = head
        count = 0

        while probe:
            count += 1
            probe = probe.next

        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # two-pointer Solution
        # step 1: traverse both both linked list and count # of nodes in both
        # step 2: assuming two linked list has length m and n, and m is the smaller one. compare the shorter linked list n nodes, with the last n nodes of the linked list with length m
        
        # length of linekd list A and B  
        m = self.getLength(headA)
        n = self.getLength(headB)

        # min and max length of the two linked list
        if m <= n:
            min_ll,max_ll = m,n
            short_ll,long_ll = headA, headB
        else:
            min_ll,max_ll = n,m
            short_ll,long_ll = headB, headA

        # set up two pointer, one at the start of shorter linked list, another one max-min away from the start position of the longer linked list
        probe_short = short_ll
        probe_long = long_ll

        for i in range(max_ll - min_ll):
            probe_long = probe_long.next
        
        while probe_short and probe_long:
            if probe_short == probe_long:
                return probe_short

            probe_long = probe_long.next
            probe_short = probe_short.next

        return None




        