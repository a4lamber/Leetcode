# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mid_node(self,head):
        # find the middle node with two pointer same-direction method;
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self,head):
        # reverse the linked List

        curr,prev = head,None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # in-place algorithm;

        # edge case when linked list is empty
        if head is None:
            return True

        # mid the pointer points to the middle of the linked list 
        half = self.mid_node(head)

        # reverse the 2nd half of the linked list
        rev_half = self.reverse(half)

        # 设置俩pointers分别在half和rev_half链表的start node
        probe_1 = head
        probe_2 = rev_half

        # boolean return for this function
        result = True

        while probe_1:
            if probe_1.val != probe_2.val:
                return False
            
            # advancing both pointer forward by 1
            probe_1 = probe_1.next
            probe_2 = probe_2.next
        
        # reverse the second half back, so input stays the same
        half.next = self.reverse(rev_half)

        return result












