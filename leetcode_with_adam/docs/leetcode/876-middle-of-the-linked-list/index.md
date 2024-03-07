---
tags:
    - Linked List
    - Two Pointers
---

# [876 Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/)

这题两种做法:

- 两个pointer `fast` and `slow`, slow走一步, fast走两步, 保证fast走到尽头的时候, slow走到中间
- 先数一遍linked list的长度, 然后再走一遍找到中间

!!! Anecdote
    2023年的我想出方法2，2024年的我想出方法1. Slowly, but getting better

俩算法复杂度都一样，都是$O(n)$ in time, $O(1)$ in space. 只不过方法1 is cleaner and one-pass while 方法2 is two-pass.

## Approach 1: Two pointers

考虑俩edge cases:

- 如果linked list为空, 那么直接返回
- 如果linked list只有一个node, 那么直接返回

之后讨论的都是linked list有至少两个node的情况. 如果for every fast advances two, slow advanced one, when it's odd, `fast.next == None`, when it's even, `fast == None`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
```


## Approach 2: Count the length of the linked list



```python
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
        mid_index = total_length//2
        counter = 0
        while counter < mid_index:
            probe = probe.next
            counter += 1
        
        return probe
```