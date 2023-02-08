# Approach 1: smart two-pointer solution 
<!-- Describe your approach to solving the problem. -->
这个解法很漂亮

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->


## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        probeA = headA
        probeB = headB

        while probeA != probeB:
            if probeA is None:
                probeA = headB
            else:
                probeA = probeA.next
            
            if probeB is None:
                probeB = headA
            else:
                probeB = probeB.next

        # if no intersection, both probe points to null
        # if intersect, both at same place
        return probeA
            
            
```



# Approach 2: normal two pointer solution
<!-- Describe your approach to solving the problem. -->

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->


## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self,head):
        # return the length of the linked list
        probe = head
        count = 0

        while probe:
            count += 1
            probe = probe.next

        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # two-pointer Solution
        # step 1: traverse both both linked list and count # of nodes in both
        # step 2: assuming two linked list has length m and n, and m is the smaller one. compare the shorter linked list n nodes, with the last n nodes of the linked list with length m
        
        # length of linekd list A and B  
        m = self.getLength(headA)
        n = self.getLength(headB)

        # min and max length of the two linked list
        if m <= n:
            min_ll,max_ll = m,n
            short_ll,long_ll = headA, headB
        else:
            min_ll,max_ll = n,m
            short_ll,long_ll = headB, headA

        # set up two pointer, one at the start of shorter linked list, another one max-min away from the start position of the longer linked list
        probe_short = short_ll
        probe_long = long_ll

        for i in range(max_ll - min_ll):
            probe_long = probe_long.next
        
        while probe_short and probe_long:
            if probe_short == probe_long:
                return probe_short

            probe_long = probe_long.next
            probe_short = probe_short.next

        return None
```

# Approach 3: Hash solution
<!-- Describe your approach to solving the problem. -->

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->


## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Hash Solution, time complexity O(m+n), space complexity O(m)
        # where m and n are the length of headA and headB respevtively.


        # create a hashmap to store
        hashtable = {}

        # two pointer, one for each linked list
        probeA = headA
        probeB = headB

        # traverse A and puts the memory address as key input the hash
        while probeA:
            hashtable[id(probeA)] = probeA.val        
            probeA = probeA.next

        # traverse b, check memory address of node in b is in the key space of the hash

        while probeB:
            if id(probeB) in hashtable.keys():
                return probeB

            probeB = probeB.next

        return None            
```

