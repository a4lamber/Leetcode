---
tags:
    - Linked List
---

# [725 Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/description/)

Split a linked list into k different linked list and each linked list should satisfies the floowing three conditions:

- length of each part should be as equal as possible
- parts occurring earlier should always have a size greater than or equal to parts occurring later
- no two parts should have a size differing by more than one

Thess conditions can be described mathematically,

- $a_1$, $a_2$,...,$a_k$ such that len($a_1$)>= len($a_2$) >= ... >= len($a_k$)
- |len($a_k$) - len($a_1$)| $\leq$ 1

where $a_k$ is k-th linked list group

## Approach 1 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
        1. length of each part should be as equal as possible
        2. a1, a2,...,ak such that len(a1)>= len(a2) >= len(a3)
        3. |len(ak) - len(a1)| <= 1
        Example:
        Case 1:
        k > len(head)
        k = 5, head = [1,2,3] if len(head) < k, then
        Case 2:
        k == len(head)
        1 each, this is trivial and mergable
        Case 3:
        k < len(head) most common
        len(head) // k as base, and append each
        """
        if not head:
            return [None for _ in range(k)]
        ll_length = self._get_length_of_ll(head)
        res = []

        # case 1: k >= ll_length
        if k >= ll_length:
            curr = head
            while curr:
                temp = curr.next            
                res.append(curr)
                curr.next = None
                curr = temp
            for _ in range(k - ll_length):
                res.append(None)
        else:
            dummy = ListNode(None,head)
            prev,curr = dummy,head

            # case 2: k < ll_length
            base_length = ll_length // k
            counter = ll_length - k * base_length
            
            while curr:
                if counter > 0:
                    start = curr
                    for _ in range(base_length + 1):
                        print(curr.val)
                        prev = curr
                        curr = curr.next
                    prev.next = None
                    res.append(start)
                    counter -= 1
                else:
                    start = curr
                    for _ in range(base_length):
                        prev = curr
                        curr = curr.next
                    prev.next = None
                    res.append(start)

        return res

    def _get_length_of_ll(self,head):        
        curr = head
        ll_length = 0
        while curr:
            ll_length += 1
            curr = curr.next
        
        return ll_length
```