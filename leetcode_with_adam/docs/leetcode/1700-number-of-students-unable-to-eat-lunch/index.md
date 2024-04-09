---
tags:
    - Array
    - Stack
    - Queue
    - Simulation
---

# [1700 Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/)

有两种学生，0 or 1, 吃一个stack of sandwiches, 0代表type 0学生爱吃，1代表type 1学生爱吃. 学生的数量和三明治数量一致，只有顶部的sandwich可以被拿走，如果学生喜欢这个sandwich，那么就可以拿走，否则就不可以拿走，问有多少学生无法吃到sandwich. 

## Approach 1 Counter

由于学生只能吃顶部的sandwich, 那么当有一方学生都拿到了自己喜欢的sandwich，比如type A. 且正好卡在了type A的sandwich上，那么剩下的type B学生就无法吃到他们爱吃的type B sandwich了, 永远卡在了下面. 

举个例子
```
students = [1,1,1,1]
sandwiches = [0,1,0,1]
```
那俩type 1学生就永远卡在了type 0 sandwich上了.

算法如下:

- 统计学生的数量
- one pass scan. Instead of moving students, we can move sandwiches. 只要该类学生还有，就可以继续移动sandwiches

### Code Implementation

```python
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        dry run:
        students = [1,1,0,0]
        counter = {
            1:2,
            0:2
        }
        Move students is same as moving sandwiches
        """
        counter = Counter(students) 
        n,k = len(students),0
        
        # traversing the sandwiches, 只要还有学生
        while k < n and counter[sandwiches[k]]:
            # found a match!
            counter[sandwiches[k]] -= 1
            k += 1
        return n - k
```

A neater solution with for loop.

```python
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students) 
        res = len(students)

        for s in sandwiches:
            if counter[s] > 0:
                res -= 1
                counter[s] -= 1
            else:
                # whoops, time to stop
                break
        
        return res
```


## Reference

- [lee](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/solutions/987403/java-c-python-easy-and-concise)
- [neetcode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=daily-question&envId=2024-04-08)