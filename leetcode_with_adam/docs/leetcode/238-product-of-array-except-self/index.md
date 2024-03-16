---
tags:
  - Array
  - Prefix Sum
---
# 238 Product of Array Except Self

这题requirements太不合理了

- O(n) in time and without using the division operation.


## Approach 1 O(n) in time, O(n) in space

There is a pattern that if the nums contains

- 0 zero, you don't worry about division by zeros
- 1 zero, only that `nums[i] = 0`, so only `ans[i] != zero`
- 2 zeros, `ans[i] = [0]*len(nums)`

You can use hashmap + above pattern to solve this problem

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # trick: 
        # no zeros, do the rolling product
        # 1 zeros, fill value at that index and fill others zero
        # 2 zeros, fill with zeros
        hashmap = set()
        for i in range(len(nums)):
            if nums[i] == 0:
                hashmap.add(i)
        
        product = 1
        ans = [0 for _ in range(len(nums))]
        if len(hashmap) == 1:
            # 1 zero in nums
            zero_index = hashmap.pop()
            for i in range(len(nums)):
                if i != zero_index:
                    product *= nums[i]
            # assign value to the only value that is not equal to zeros
            ans[zero_index] = int(product)
        elif len(hashmap) == 0:
            # no zeros in nums            
            # initialize
            for i in range(1,len(nums)):
                product *= nums[i]
            ans[0] = product
            # update
            for curr in range(1,len(nums)):
                product = product * nums[curr-1] / nums[curr]
                ans[curr] = int(product)
        
        # do nothing for >= 2 zeros
        return ans
```

## Approach 2 O(n) in time, O(1) in space

With the trick above, you don't even need to use hashmap. Just use a counter to count the number of zeros in the nums. 

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_of_zeros = 0
        zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                num_of_zeros += 1
                zero_index = i
        
        product = 1
        ans = [0 for _ in range(len(nums))]
        if num_of_zeros == 1:
            # 1 zero in nums
            for i in range(len(nums)):
                if i != zero_index:
                    product *= nums[i]
            # assign value to the only value that is not equal to zeros
            ans[zero_index] = int(product)
        elif num_of_zeros == 0:
            # no zeros in nums            
            # initialize
            for i in range(1,len(nums)):
                product *= nums[i]
            ans[0] = product
            # update
            for curr in range(1,len(nums)):
                product = product * nums[curr-1] / nums[curr]
                ans[curr] = int(product)
        
        # do nothing for >= 2 zeros
        return ans
```