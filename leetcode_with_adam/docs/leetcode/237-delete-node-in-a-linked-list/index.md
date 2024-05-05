---
tags:
    - Linked List
---

# 237 Delete Node in a Linked List

## Approach 1: 


移除node的两个方法:

- `Approach 1`: given only `node`, 将node的值替换为下一个node的值，然后跳过下一个node
    - node.val = node.next.val
    - node.next = node.next.next
- `Approach 2`: 双指针法, 将node的上一个指针指向下一个node. given `head` of linked list and `node` to delete
    - prev.next = node.next
    - 这个方法需要generalize treatment for first node and interior node. 加一个dummy header node可以简化这个问题

### Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```