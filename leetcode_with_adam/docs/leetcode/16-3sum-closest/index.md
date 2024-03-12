
# 16 3 Sum Closest


## Approach 1 Brute Force

暴力解就是enumerate所有的triplet, 然后找到离target最近的那个triplet.

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # exactly one solution!!
        # Brute force: 
        # 1. find all arbitary three elements that match the condtion (enumeration)
        # 2. run through all of them to see which is closest
        
        n = len(nums)
        res = []
        curr = 1e5
        for i in range(n):
            for j in range(i):
                for k in range(j):
                    candidate = nums[i] + nums[j] + nums[k] - target
                    if abs(candidate) < abs(curr):
                        curr = candidate
        return curr + target
```

## Approach 2 Sorting + Two Pointers


```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):
            lo,hi = i+1,len(nums)-1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                # maintain the diff
                if abs(target - curr_sum) < abs(diff):
                    diff = target - curr_sum
                
                # 判断是否要变大还是变小
                if curr_sum == target:
                    break
                elif curr_sum < target:
                    lo += 1
                else:
                    hi -= 1
            
        return target - diff
```