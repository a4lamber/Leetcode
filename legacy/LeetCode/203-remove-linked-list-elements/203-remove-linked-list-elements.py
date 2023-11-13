# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy node求解模式
        dummy_node = ListNode(val = None,
                              next =None)
        # point this node to next node
        dummy_node.next = head
        
        # 设置两个pointer prev and curr
        # 分别记录previous location and current location
        prev,curr = dummy_node,head

        while curr:
            if curr.val == val:
                # 发现target了
                prev.next = curr.next
            else:
                # prev往前走一步
                prev = curr
            # curr往前走一步
            curr = curr.next
            



        return dummy_node.next