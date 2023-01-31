# Readme

## Intuition
在LC第一题`1-two-sum`中学过的one pass hash, trade space for speed. Works like a charm.


## Approach

One-pass hash approach, 在initialize an hash by traverse through the array, during each iteration, do the following two:
- check if the current element in the array in the key space of the hash
  - if yes, that's duplicate element. Need to append it to the output list
  - if no, moves on
- assign the element to the array to the key of the hash and index as value such as `value:key` 

## Complexity

- 空间复杂度: $O(n)$
- 时间复杂度: worst case and average case $O(n)$


## Code
```python
"""
Condition: each integer appears once or twice.
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # declare a hash and output
        hashtable = {}
        output = []

        # one-pass hash
        for i in range(len(nums)):
            # check if current element in the hash 
            if nums[i] in hashtable:
                # append to output
                output.append(nums[i])
            # assign value to hash
            hashtable[nums[i]] = i 
        
        return output
```