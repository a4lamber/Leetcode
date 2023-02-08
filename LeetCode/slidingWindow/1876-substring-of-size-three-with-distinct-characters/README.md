# Approach 1 Hash
First thing pops in my head after seeing checking duplicate in subarray is to ues hash, so i divide the problem into two parts:
- determine whether all characters within the window are different from each other, returns boolean. This is handled in `isGood()` method
- traverse the string

## Code
```python
class Solution:
    def isGood(self,window):
        # return whether all three chars are different to each other
        # create a dictionary
        sliding_hash = {}
        
        # traverse the window
        for i in range(3):
            if window[i] not in sliding_hash:
                sliding_hash[window[i]] = 1
            else:
                return False

        return True

    def countGoodSubstrings(self, s: str) -> int:
        # output
        res = 0
        # traverse the string 
        for i in range(0,len(s)-2):
            # determine wether it's unique
            if self.isGood(s[i:i+3]):
                res += 1
        return res
```

# Approach2: Sliding Window
<!-- Describe your approach to solving the problem. -->
Sliding window, a technique that is used to minimize the number of redundant traversal or scan over the item in array or string. In this problem, when window slides forward by one, you need to:
- remove the last element 
- take in new element in the direction of moving

To achieve the above two operations, just shuffle everything forward by one like how insert and remove work in static array. 


## Code
```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # sliding window approach

        # edge case
        if len(s) < 3:
            return 0
            
        # output
        res = 0
        # declare three variables
        a,b,c = s[0],s[1],s[2]

        # compare within the window, then slide forward by 1
        for i in range(0,len(s)-2):
            # determine whether char in window are mutually different
            if a != b and b!=c and a!=c:
                res += 1
            
            # for the last window, you don't need to slide forward since it's over
            if i+3 != len(s):
                a = b
                b = c
                c = s[i+3]
        
        return res
```

