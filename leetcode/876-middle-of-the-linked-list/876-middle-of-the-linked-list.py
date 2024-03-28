# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_length(self, head):
        """
        return the total length of the linekd list
        """
        length = 0
        probe = head
        while probe != None:
            length += 1
            probe = probe.next
        return length

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 计算linked list的总长度
        total_length = self.get_length(head)

        # 无论奇数还是偶数，用floor division都能一样处理
        probe = head
        mid_index = total_length // 2
        counter = 0
        while counter < mid_index:
            probe = probe.next
            counter += 1

        return probe
