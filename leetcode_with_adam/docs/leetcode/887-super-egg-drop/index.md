---
tags:
    - Math
    - Binary Search
    - Dynamic Programming
---

# [887 Super Egg Drop](https://leetcode.com/problems/super-egg-drop/description/)

这一题相当难，我的intuition是binary search, 这样的话solution就应该是$O(\log_2\left(n\right))$. 但题目中还有$k$个鸡蛋，不可能是没用的信息。假设我们只有一颗鸡蛋的话，我们根本没办法binary search, 唯一能够做的策略就是从第一层开始，一层一层的试，直到鸡蛋碎了。这样的话，我们的solution就是$O(n)$. 你可以把鸡蛋想象成你有的资产，你投资的策略有两个极端:

- 极端保守: 一层一层的试，直到鸡蛋碎了，也就确认了. 效率低但保险，最多只损失一颗鸡蛋.
- `binary search`: 二分法，每次试一半，直到找到答案, 效率极其高, 损失鸡蛋数量在最坏情况下是$\log_2\left(n\right)$.

随着给予你的`(k,n)`, 你的策略应该是在这两个极端之间找到一个平衡点. 所以这一题又是一个优化的问题

!!! tip
    资产越多，你就越有能力去承担风险，也就是说你可以更加aggressive. 资产越少，你就越应该保守，因为你的损失是不可承受的. 从leetcode看财富.





# Reference

- [huahua](https://www.youtube.com/watch?v=aPY6sps_Q44&ab_channel=HuaHua)