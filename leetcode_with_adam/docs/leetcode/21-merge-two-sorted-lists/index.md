---
tags:
    - Linked List
    - Recursion
---

# 21. Merge Two Sorted Lists

## Approach 1: iterative approach
<!-- Describe your approach to solving the problem. -->
merge two sorted list, as one of the most classic problem, 有挺多测试的点的, 需要不断比较两个链表中的最小值,直到一个链表reach null.

假设两个链表，它们的值分别是$a_i$ and $b_i$, respectively. 有需要简化的是，将$a_i$ = $b_i$的情况，归入$a_i$<$b_i$ 的情况

- $a_i$ = $b_i$ (这种情况可以归入a<b中)
- $a_i$ < $b_i$
- $a_i$ > $b_i$

合并后为:

- $a_i\leq$  $b_i$
- $a_i >$  $b_i$

算法思路如下:

- create a dummy node as the start of result linked list
- create two pointers, `head` and `tail` which points to the start and end of the linked list respectively.
- compare $a_i$ and $b_i$ then,
  - connect the `tail` with linked list with $min(a_i,b_i)$ (in this step, you add one more node into your result linked list)
  - advance the linked list with $min(a_i,b_i)$
  - advance the tail by one
- append the remaining nodes to the `tail` of merged list


## Complexity
- Time complexity: $O(m+n)$, m and n are the # of nodes in each linked list, respectively
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Code Implementation

```python
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
```


## Approach 2: recursive approach

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```