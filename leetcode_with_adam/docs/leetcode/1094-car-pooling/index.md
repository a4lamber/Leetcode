---
tags:
    - Array
    - Sorting
    - Heap
    - Simulation
    - Prefix Sum
---

# [1094 Car Pooling](https://leetcode.com/problems/car-pooling/description/?envType=company&envId=lyft&favoriteSlug=lyft-three-months)



## Approach 1 Sweep Line

扫描线 + interval的，比较经典, 和meeting room, 打飞机是一样的题目,具体思路如下


- 维护一个sorted queue, `[(num_passenger, time,status),(num_passenger, time,status)]`, 保证time是`ASC`, 保证status是getting off排在getting in之前
  - assume status == 1, then getting in. status == 0 then getting off
- traverse the sorted queue, 维护一个int记录free seat


!!! note
    passengers是先下后上，有序候车, 所以需要sort first by time, then by (getting off > getting in)

### Code Implementation

```python
from collections import deque
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        for trip in trips:
            num_passanger,from,to
        Questions:
            - is the trips data set sorted?
            - input range is 1 to 1000, so it's most likely gonna be > linear
            O(nlogn) -> O(n^2)
        As we driving
        - int: keep track of capacity +2, -1 to see if it's gonna ba enough
        
        """
        array = []
        for trip in trips:
            num,start,end = trip
            # ppl getting in to the car
            array.append((num,start,1))
            # ppl getting off the car
            array.append((num,end,-1))
        # make sure if there is a tie in get-in and get-off, we always calculate
        # get off first
        
        array.sort(key = lambda x: (x[1],x[2]))

        # convert it to deque
        queue = deque(array)
        free_seats = capacity
        
        while queue:
            num,time,status = queue.popleft()
            if status == 1:
                # get in the car
                free_seats -= num
            else:
                # get off the car
                free_seats += num
            if free_seats < 0:
                return False
        
        return True
```


## Approach 2 Bucket Sort

Bucket sort, 把无限的问题转化为有限的问题，通常需要基于你对这个问题的理解, 常见问题比如

- count frequency of alphabet in a string

我们维护一个array of size 1001, 记录每一个时间点的aggregated passenger变化数量, 

$$
\begin{equation}
bucket = [\Delta p_0,\Delta p_1,\Delta p_2,\dots,\Delta p_{1001}]
\end{equation}
$$
where $\Delta p_t$ is the change of passenger at timestamp t.

!!! note
    这个解法和讨论是有意义的，因为

    - 如果不是carpool, 而是bus, 你stop的terminals数量是finite的. 
    - 把无限的问题转化为有限的.
    
    这个解法更为优雅，不仅是效率提高，而且不需要sort两次很搞脑子的，因为我们把问题简化了，从

    - 每一次客人上下车后，车是否能载的下
  
    转化为

    - 每一站，全部上完下完后，我的车里会新增几人?

    是更优雅的逻辑.


### Code implementation

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        problem bound infinite domain > finite domain 
        
        0 <= from < to <= 1000
        So we can change the problem to be a bounded problem, using
        auxillary DS list, bucket of size 1001 to maintain the        
        change in customer at each timestamp, 
                  0  1. 2. 3....1000
        bucket = [0, 1, 3, 5 ]
        
        If at any timestamp, we have our data 

        """
        bucket = [0 for _ in range(1001)]
        
        for trip in trips:
            num,start_t,end_t = trip            
            bucket[start_t] += num
            bucket[end_t] -= num

        num_passenger = 0

        for delta_passenger in bucket:
            num_passenger += delta_passenger
            if num_passenger > capacity:
                return False
        return True
```