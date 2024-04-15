# [3111 Minimum Rectangles to Cover Points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/)

## Approach 1

我们需要找到多少个maximum width为w的, bottom在x-axis上的rectangle do we need to cover all the points. 

以下几点需要注意:

- rectangle可以无限高，所以y value of point没有意义。只care about x value
- duplicate x value没有意义，因为我们可以用一个rectangle cover多个在同一条竖线的点

算法逻辑如下:

- 或者x values, 去重，然后sort
- initialize left,right boundary of the first rectangle
- traverse the sorted x values, 
    - 如果当前的x value在left,right之间，那么我们不需要新的rectangle，
    - 如果当前x value超过right boundary, 我们需要新的rectangle，更新left,right boundary并且counter + 1


```python
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        """
        objective: 多少个maximum width为w的, bottom在x-axis上的rectangle do we need
        to cover all the points
        Observation:
        - 存在width == 0的rectangle
        - height无所谓
        - 10^5, so it hightly likely O(nlong) at most and most likely O(n). Gonna be a gready
        - simulation
        """
        seen = set()
        arr = []
        for point in points:
            x,_ = point
            if x in seen:
                continue
            arr.append(x)
            seen.add(x)
        # sort it
        arr.sort()
        
        left,right = arr[0],arr[0] + w
        i = 0
        res = 1
        while i < len(arr):
            if arr[i] >= left and arr[i] <= right:
                i += 1
            elif arr[i] > right:
                # update left, right boundary
                left,right = arr[i],arr[i] + w
                res += 1
                
        return res
```
