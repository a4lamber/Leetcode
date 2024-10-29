---
tags:
    - Array
    - Linked List
    - Matrix
    - Simulation
---

# 2326 Spiral Matrix

## Approach 1 Simulation

After drawing a matrix and draw the CW spinning spiral, we find out the following pattern:

- it moves right n step
- it moves downward m-1 step
- it moves left n-1 step
- it moves up m-2 step
- it moves right n-2 step
- ...

We could do the following:

- create a outer loop to repeat `right` --> `down` --> `left` --> `up`
- Each time move horizontally, the moving distance reduces by one. True for vertical movement as well



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """
        - if check length of the ll and comapre with mxn, if len(ll) < m*n, fill with -1
        moving logic, 
        right, downward, left, upward
        if we have i, j for m and n
        right: j == n-1
        downward: i == m-1
        left: j == n
        """
        res = [[-1 for _ in range(n)] for _ in range(m)]
        
        ll_length = 0
        curr = head
        while curr:
            ll_length += 1
            curr = curr.next

        curr = head
        i,j = 0,-1
        horizontal_step,vertical_step = n,m-1
        orders = ["right","down","left","up"]

        # 以curr是否为空判定是否脱离
        while curr:
            """
            move in a order of 
            right,down,left,up
            with moving distance
            round 1: n,m-1,n-1,m-2,            
            round 2: n-3
            
            """
            if not orders:
                # reset, 2周目
                orders = ["right","down","left","up"]
            if orders[0] == "right":
                for _ in range(horizontal_step):
                    j += 1
                    res[i][j] = curr.val                   
                    curr = curr.next
                    if not curr:
                        break
                orders.pop(0)
                horizontal_step -= 1
                continue
            if orders[0] == "down":
                for _ in range(vertical_step):
                    i += 1
                    res[i][j] = curr.val
                    curr = curr.next
                    if not curr:
                        break
                orders.pop(0)
                vertical_step -= 1
                continue
            
            if orders[0] == "left":
                for _ in range(horizontal_step):
                    j -= 1
                    res[i][j] = curr.val
                    curr = curr.next
                    if not curr:
                        break
                orders.pop(0)
                horizontal_step -= 1
                
                continue
            
            if orders[0] == "up":
                for _ in range(vertical_step):
                    i -= 1
                    res[i][j] = curr.val
                    curr = curr.next
                    if not curr:
                        break
                orders.pop(0)
                vertical_step -= 1
                continue
        return res   
```
