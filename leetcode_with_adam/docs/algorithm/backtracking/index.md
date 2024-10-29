# Backtracking 回溯

## Intuition

回溯算法，是基于recursion的，专用用于解决constraint satisfaction problems (CSPs),比如

- sudoku
- maze problem

这个算法是generate一系列partial candidates, 如果不符合constrain, 就abandon current solution and backtrack.

通常解都会是一个tree的形式(类似DFS), 但是是一个conditional DFS. 高中就学过的permutation (也叫combination tree), 就是一个没有constrains的backtracking solution.

![](https://i.sstatic.net/pyzZV.jpg)

We need these things,

- `escape condition (if)`: similar to the base case in recursion
- `constraint satisfaction (if)`: conditionally decide whether we want the partial solution or not. All sorts of if condition
- `i`: track which layer we at
- `path`: state variables that record the partial solution

Template

```python
def backtrack(node,state):
    # base escape
    if state is a solution:
        res.append(state)
        return
    
    for i in range:
        # insert your condition here
        if i is one solution:
            state.append(i)
            backtrack(i+1,state)
            state.remove(i)
```



|number|condition|description|solution|
|---|---|---|-|
|17 letter combinations of a phone number|-|-|-|
|[39 Combination Sum](https://leetcode.com/problems/combination-sum/description/)|
|46 Permutations|
|47 Permutations II|
|51 N-queen|
|[78 subsets](https://leetcode.com/problems/subsets/description/)|
|[90 subsets II](https://leetcode.com/problems/subsets-ii/description/)|


# Reference

- [backtracking template](https://www.youtube.com/watch?v=h6nfiZCF0r4&t=1s&ab_channel=Sasacodes)
- [Backtracking (Think like a programmer)](https://www.youtube.com/watch?v=gBC_Fd8EE8A&ab_channel=V.AntonSpraul)