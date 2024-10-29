---
tags:
    - String
    - Backtracking
    - Dynamic Programming
---

# [22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)


## Approach 1 Backtracking

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

先枚举几个例子

```
n = 1
["()"]
n = 2
["()()","(())"]
n = 3
["()()()","(()())","(())()","()(())","()()()"]
```

注意到以下pattern:

- `(`和`)`数量一致

哈哈，并没有那么helpful, 但这是我第一眼得到的insight

那我们来一个暴力解，会是什么样的呢, 其实是个概率题, 假设为`n = 3`, 那正确答案必然在 `_,_,_,_,_,_`每个slot有两种可能， either `(` or `)`， 那么我们一共有$2^6$种可能性，其中只有5个是well formed解. 那我们面临的问题是,

- 暴力求解exhaust $2^6$种可能性
- 怎么在数学上定义well-formed Parentheses

我们试着缩小这$2^6$的可能性，方法为利用注意到的pattern, `(`和`)`数量一致, 我们假设的每个slot都有两种可能性就被缩小了, 定义为

!!! note
    假设为`n = 3`, 那正确答案必然在 `_,_,_,_,_,_`每个slot有两种可能， either `(` or `)`. 也就是`(`或者`)`都出现三次, 也就是6个坑位选3个放`(`.
    $$
    \begin{equation}
        C_{6}^{3} = \frac{n!}{(r!(n-r)!)} = 20
    \end{equation}
    $$
    这样就能确定`(`.

    枚举一下,
    ```
    ((()))
    (()())
    (())()
    ()(())
    ()()()
    ((())
    (()()
    (())(
    ()(()
    ()()(
    ())((
    ())()
    ()())
    )()(()
    )()()(
    ))((()
    ))(())
    ))()()
    )()))(
    )))(((
    ```

那我们解的数量reduce from $2^6$ --> 20. Can we Do better? 从[20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) 和观察上面的规律可知,

!!! tip
    Every close bracket `)` must have a `(` before it. Or in another words, `)`的出现次数必须<= `(`的出现次数

那我们这题的限制条件量化为数学语言就是，在solution生成的过程中, candidate solution必须符合

- `(` and `)`的出现次数不能超过$n$次
- `)`的出现次数必须<= `(`的出现次数

用这两个条件可知，我们在生成的backtrack的条件为

```
if close_cnt < open_cnt:
    生成生成!
if open_cnt < n:
    生成生成!
```



### Code Implementation

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        problem:
        n = 1
        ["()"]
        n = 2
        ["()()","(())"]
        n = 3
        ["()()()","(()())","(())()","()(())","()()()"]

        n = 1
            (
         ()   ((
              not working         
        n = 2
                (
            ((      ()
        
        (()   (((

     (()( (())
        Pattern: 所有well-formed parathese, 在从左到右scan的过程中，
        左边括号的数量 >= 右边括号的数量

        假设，我们recursively生成一个字符串, 每一次action,we either
        - add a "("
        - add a ")"
        但生成过程中的限制条件:
        - left_cnt is bounded by [0,n]
        - rifht_cnt is bounded by [0, left_cnt]
        """
        

        def backtracking(curr,open_cnt,close_cnt):
            # escape condition,when we reach bottom
            if len(curr) == 2*n:
                res.append("".join(curr))

            if close_cnt < open_cnt:
                curr.append(")")
                backtracking(curr,open_cnt,close_cnt + 1)
                curr.pop()
            if open_cnt < n:
                curr.append("(")
                backtracking(curr,open_cnt + 1,close_cnt)
                curr.pop()

        res = []
        backtracking(curr = [],open_cnt = 0,close_cnt = 0)
        return res
```