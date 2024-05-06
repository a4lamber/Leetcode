---
tags:
    - Linked List
    - Stack
    - Recursion
    - Monotonic Stack
---


# 2487 Remove Nodes From Linked List

两个解法:

- monotonic stack, 维护一个单调递减的stack, 用来存储保留的node, 之后rebuild. 时间复杂度O(n), 空间复杂度O(n)
- reverse, 最优解，但是需要modify input linked list in-place. 时间复杂度O(n), 空间复杂度O(1)


## Approach 1: Monotonic Stack


### Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        while curr:
            while stack and curr.val > stack[-1].val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        # rebuild the linkedlist
        dummy = ListNode(None,None)
        curr = dummy
        
        for node in stack:
            curr.next = node
            curr = node
        return dummy.next
```

## Approach 2: Reverse

对于每一个node来说，是否需要删除，只需要看它的右边是否有比它更大的node即可，如下图,

![](./assets/1.excalidraw.png)

显然发着traverse比较方便，所以我们可以:

- 先reverse linked list
- 从左到右traverse, 如果右边有比当前node更大的node, 则删除当前node
- 最后再reverse回来

### Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev,curr = None,head
            while curr:
                temp = curr.next
                curr.next = prev
                prev,curr = curr,temp
            return prev
        
        head = reverse(head)
        curr = head
        curr_max = curr.val

        # curr是必然会被保留下来的
        while curr.next:
            if curr.next.val < curr_max:
                # 删掉curr.next
                curr.next = curr.next.next
            else:
                # 更新curr_max, 走一格
                curr_max = curr.next.val
                curr = curr.next                
        return reverse(head)
```