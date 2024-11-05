---
tags:
    - Array
    - Heap
---

# [1882 Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/description/?envType=company&envId=lyft&favoriteSlug=lyft-all)


## Approach 1 Two min heap

这题提示了很多需要用heap,

> As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index

这就意味着我们的auxillary要有一定的自动排序功能，且会频繁的access its minimum, 所以min heap.

- construct a min heap for free_servers and busy_servers
  - `free_servers = [(weight,idx),(weight,idx),....]`
  - `busy_servers = [(next_available_time,weight,idx), (next_available_time,weight,idx),...]`
- we traverse the `tasks`, and in each step we
  - check `busy_servers` to see if anything free and move to `free_servers` until no more busy_server, or first-available server is still not available. Delayed updates
  - assign tasks
    - if there are free_server, we just move the first available server and move it to busy_servers, Delayed updates
    
!!! tip
    我最初的思路是simulate until all tasks done. 但计算`ans[]`, 只需要到我们schedule完`tasks[-1]`即可, 这样就not only depends on tasks but also `max(tasks[i])`了.


```python
from collections import deque
from heapq import heapify,heappush,heappop
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        (min_weight,min_index)
        ans[j]: jth task will be assigned to which server
         0 1 2 3 4 5
        [2,2,0,2,1,2]
                   0,1,2
        servers = [3,3,2]
        
        [(2,2),(3,0),(3,1)
        """
        # minheap of (server_weight,server_idx,next_free_time)
        free_servers = [(weight,i) for i,weight in enumerate(servers)]
        heapify(free_servers)

        # (end_time, weight,idx)
        ans,busy_servers = [],[]

        for time,task in enumerate(tasks):
            # delayed clearing on free_server 
            while busy_servers:
                # peek 
                free_time,weight,idx = busy_servers[0]
                # 无法清空
                if time < free_time:
                    break
                heappush(free_servers,(weight,idx))
                heappop(busy_servers)
            
            if not free_servers:
                # when no more free servers
                end_time,weight,idx = heappop(busy_servers)
                # increments the end time
                heappush(busy_servers, (end_time + task,weight,idx))
            else:
                # 还有空server
                weight,idx = heappop(free_servers)
                heappush(busy_servers,(time + task,weight,idx))
            # assign server
            ans.append(idx)
        return ans
```