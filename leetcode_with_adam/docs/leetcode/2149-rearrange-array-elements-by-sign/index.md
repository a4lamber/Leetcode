
# [2149 Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14)

## Approach 1 Hash $O(n)$ in space and time

```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        hashmap = {"p":[],"n":[]}
        for num in nums:
            if num > 0:
                hashmap["p"].append(num)
            else:
                hashmap["n"].append(num)
        
        res = []
        half_length = int(len(nums)/2)
        for i in range(half_length):
            res.append(hashmap["p"][i])
            res.append(hashmap["n"][i])
        
        return res
```

## Approach 2