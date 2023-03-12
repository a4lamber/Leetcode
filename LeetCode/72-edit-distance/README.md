
# Approach 1: bottom up

It is simliar to LCS and we need to define DP first

- `DP[i,j]`: the minimum edit distance needed between word1 and word2.
- `base case`: including the consideratio of $\varnothing$, then any word modified to $\varnothing$ would be `len(word)`
- case 1: when `word1[i] == word2[j]`, then informatin is from top left corner
- case 2: when `word1[i] != word2[j]`, the information is coming from the minimum out of top cell, left cell or top left cell. And we need do one most operation to replace `word1[i]` and `word2[j]`

$$
DP[i,j] = \begin{cases}
    i&if\,j=0\\
    j&if\,i=0\\
    DP[i-1,j-1]&if\,word1[i] = word2[j]\\
    min(DP[i-1,j-1],DP[i-1,j],DP[i,j-1])&if\,word1[i] \neq word2[j]\\
\end{cases}
$$

I would do an example so you could visualize it by first initializing it.

|-|$\varnothing$|r|o|s|
|-|-|-|-|-|
|$\varnothing$|0|1|2|3|
|h|1|-|-|-|
|o|2|-|-|-|
|r|3|-|-|-|
|s|4|-|-|-|
|e|5|-|-|-|

The rest of it is extremely similar to the LCS example so i won't bother
.
## Code implementaton

```python
from collections import defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP[i,j]: the minimum number of operations needed to edit from word1 to word2;
        # base case: 如果任何一个substring为空集，# of ops needed to reach 空集 always will be len(other_words);
        # case 1: if word1[i] == word2[j], then no editing needed from upper left corner
        # case 2: if word1[i] != word2[j], min(top cell, topleft cell, left cell)
        # 由于定义是min # of operations needed, 那么信息可以从任一previous step流动过来

        x = len(word1) 
        y = len(word2)

        # 加入空集的考量，就不用treat边界 and mid nodes different了
        DP = defaultdict(int)

        for i in range(x+1):
            DP[(i,0)] = i
        
        for j in range(y+1):
            DP[(0,j)] = j

        # horizontal scanning, left to right, top to bottom
        for i in range(1,x + 1):
            for j in range(1,y + 1):
                # 判断是否相等
                if word1[i-1] == word2[j-1]:
                    # info is propogating from top left 
                    DP[(i,j)] = DP[(i-1,j-1)]
                else:
                    # info is propogating from top or left
                    DP[(i,j)] = 1 + min(DP[(i-1,j)],DP[(i,j-1)],DP[(i-1,j-1)])

        return DP[(x,y)]
```

> food for thought, what if you can only do delete and insert? 

## If only `delete` and `insert` allowed
In only delete and insert allowed, you can reduce the problem to the classics LCS problem. 

```python
from collections import defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # similar to LCS, find the largest common substring between word1 and word2,
        # then 
        # example: "horse", "ros", --> LCS ="os". len(word1) - len(LCS) = 5 - 2 = 3
        # example: "intention", "execution", --> LCS ="tion". len(word1) - len(LCS) = 9 - 4 = 5

        # initialize to be zeros
        
        x = len(word1) 
        y = len(word2)

        # 加入空集的考量，就不用treat边界 and mid nodes different了
        LCS = defaultdict(int)

        # horizontal scanning, left to right, top to bottom
        for i in range(1,x + 1):
            for j in range(1,y + 1):
                # 判断是否相等
                if word1[i-1] == word2[j-1]:
                    # info is propogating from top left 
                    LCS[(i,j)] = LCS[(i-1,j-1)] + 1
                else:
                    # info is propogating from top or left
                    LCS[(i,j)] = max(LCS[(i-1,j)],LCS[(i,j-1)])
        # replace operation: 最划算，相当于delete 1 char + add 1 char
        # insert operation: 增加一个数字
        # delete operation: 减少一个数字
        # 怎么样计算replace a character的number of opetaion呢?
        
        edit_distance = len(word1) - LCS[(x,y)] + len(word2) - LCS[(x,y)]
        return edit_distance
```










## Reference