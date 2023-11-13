# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
感觉这题用python的built-in function, `string.replace()` 有些cheating.


# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        output = address.replace(".","[.]")
        
        return output
```