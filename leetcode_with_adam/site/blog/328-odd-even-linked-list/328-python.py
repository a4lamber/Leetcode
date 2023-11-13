# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # one pass solution with O(n) in time, O(1) in space;
        
        # the head of the linked list consists of only even nodes
        
        # corner cases when it only has one or two nodes (no operations needed)
        if head is None or head.next is None:
            return head
        


        # two pointers
        odd = head
        even = head.next

        # 偶数链表的头
        evenhead = head.next
        while even and even.next:
            # 连接奇数点和偶数点
            odd.next = odd.next.next
            even.next = even.next.next
            # advance both pointers by one
            odd = odd.next
            even = even.next

        # 将奇数列表的尾和偶数链表的头连接在一起
        odd.next = evenhead

        return head    



