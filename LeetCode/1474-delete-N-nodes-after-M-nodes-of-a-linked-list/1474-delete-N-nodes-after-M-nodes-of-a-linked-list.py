# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # 创造一个dummy node
        dummy_node = ListNode(val = None,next = None)
        dummy_node.next = head

        # 设置两个指针，记录当前时间步和上一个时步
        prev, curr = dummy_node,head

        while curr:
            for i in range(m):
                if curr:
                    # shuffule forward
                    prev = curr
                    curr = curr.next
                else:
                    return dummy_node.next

            for j in range(n):
                if curr:
                    # remove node
                    prev.next = curr.next
                    # shuffle forward
                    curr = curr.next
                else:
                    return dummy_node.next

        # edge cases: len(head)%(m+n) == 0
        return dummy_node.next