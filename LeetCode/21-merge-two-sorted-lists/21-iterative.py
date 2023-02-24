# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create two dummy ListNode
        tail = ListNode(None)

        head = tail
        # tip: 小的往前走一步
        while list1 and list2:
            if list1.val <= list2.val:
                # case: l1.val <= l2.val
                tail.next = list1
                list1 = list1.next
            else:
                # case: l1.val > l2.val 
                tail.next = list2
                list2 = list2.next
            
            # advance merged list by one
            tail = tail.next

        # 在这个阶段,总共两种情况:
        # 1. list1 is None, list2 != None
        # 2. list2 is None, list1 != None
        if list1 != None:
            # list1中剩余的数，都比merged list中的大
            tail.next = list1
        else:
            # list2剩余的数，都比merged list中的大
            tail.next = list2

        return head.next