# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Very classy way of using hash to find duplicate.

# Approach
<!-- Describe your approach to solving the problem. -->
略


# Complexity
- Time complexity: $O(n)$ assuming good implemention of hash
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #
        hashtable = {}

        for i in range(len(nums)):
            # check if current element
            if nums[i] in hashtable.keys():
                return True

            # assign key-value pair as value-index 
            hashtable[nums[i]] = i
        
        return False
```