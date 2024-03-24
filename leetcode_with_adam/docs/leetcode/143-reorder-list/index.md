---
tags:
    - Linked List
    - Two Pointers
    - Stack
    - Recursion
---

# 143 Reorder List

You are given the head of a singly linked-list. The list can be represented as:

> L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

> L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.


## Approach 1 Two Pointers

根据题目要求，一头一尾依次连接，那其实很自然想到two pointers on both ends, 然后做一些node manipulation. 但由于题目给定的是singly linked list, 所以我们没办法traverse backward, 那就必须要用点hacky way让我们可以traverse backwards, 因此我的思路源自于为了创造, 一个可以traverse backwards的结构，思路如下

- reverse second half of the linked list, 思路和[234 Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)一样
    - two pointers to find mid point (same direction, fast and slow)
    - implement the REVERSE THE LINKED LIST
- reverse the 2nd half of the linked list
- two pointer techniques to rearrange until they meet

!!! 注意事项
    meeting condition要分类讨论，

    - 如果是奇数个node，`left is right`
    - 如果偶数个node，`left.next is right`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1. thinking two pointers, on either ends. 为了利用two pointers in singly linked list
        , we have to do something since it can't traverse backward
        Steps:
        1. reverse second half of the linked list
            1.1 two pointers (same direction, fast and slow to find mid point)
            1.2 implement the REVERSE THE LINKED LIST MEME
        2. two pointer techniques
        """        

        # 1.1 find mid point
        mid = self.get_mid(head)
        # 1.2 reverse
        right = self.reverse(mid)        
        left = head
        

        while (left is not right) and (left.next is not right):
            l_next = left.next
            r_next = right.next
            
            left.next = right
            right.next = l_next

            # update pointers
            left = l_next
            right = r_next
        
        return head    
    
    def get_mid(self,head):
        """
        return the middle node of the linkedlist list given head of LL
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse(self,head):
        if not head or not head.next:
            return head
        
        curr,prev = head,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
```

## Approach 2 Stack

各种reverse的情况，能想到stack，因为stack是先进后出，所以可以用stack来存储node，然后pop出来，这样就可以实现reverse的效果。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        start = head
        while start:
            end = stack.pop()
            if start is end:
                # odd case
                start.next = None
                break
            elif start.next is end:
                # even case
                start.next = end
                end.next = None
                break
                
            
            temp = start.next
            start.next = end
            end.next = temp
            # update
            start = temp
            
            # if start is not None and start.next == end:
            #     start.next = None
            #     break
            
        return head
```


[网友opendrum](https://leetcode.com/problems/reorder-list/editorial/comments/718547)用了另一种判定方法，我也学些了一下，这种方法更简洁，不用分类讨论，直接判断start.next is end即可。它的判定在末尾(我还是没理解为什么`start is not None`)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        start = head
        while start:
            end = stack.pop()
            temp = start.next
            start.next = end
            end.next = temp
            # update
            start = temp
            
            if start is not None and start.next == end:
                # start.next == end for odd case
                # what about start is not None???
                start.next = None
                break
            
        return head
```