---
tags:
    - Array
    - Simulation
    - Interactive
---

# [157 Read n Characters Given read4()](https://leetcode.com/problems/read-n-characters-given-read4/description/)


158的铺垫题，难点在于理解read4(),以及答案要求什么.

As for read4, it is defined as 
```
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
```

你需要通过implement read(buf,n) to call read4(buf4) to access the characters in the file. 也就是说，我们实现的`read()`, 需要一直call `read4()`, 直到某种条件被达成为止, 接下来我们思考怎么想到termination条件


单独考虑`read4(buf4)`我们一共有三种case:

- read(4) returns 4, 读取了所有的数据
- read(4) returns 1-3, 说明file快读完了，只能再读一次了
- read(4) returns 0, file has been read completely

同时考虑`read(buf,n)` and `read4(buf4)`

- 读n个characters的条件已经被满足了

综上所述，我们需要考虑的termination condition为

- n characters 被读完了
- read(4)的return < 4

## Approaches 

- maintain two variable and initialize them to be `copied_char_so_far = 0` and `read_4_res = 4`
    - `copied_char_so_far` a pointer in `buffer`, keep track of how many characters we have copied so far. 
    - `read_4_res` the return value of the last time `read4()` has been called.
- while condition on `copied_char_so_far` and `read_4_res`
    - a nested loop to copy everything from `buf4` to `buf`
    - increment by `copied_char_so_far` by 1

!!! note
    题目给了You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters. 所以不需要扩容array size.

## Code Implementation

```python
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file

Appraoches:
- You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
- call read() only
- Use read() to call read4() to access file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = ['' for _ in range(4)]
        copied_so_far = 0 # counter < n
        to_read = 4

        while copied_so_far < n and to_read == 4:
            to_read = read4(buf4)

            for i in range(to_read):
                if copied_so_far == n:
                    break
                buf[copied_so_far] = buf4[i]
                copied_so_far += 1
        return copied_so_far
```