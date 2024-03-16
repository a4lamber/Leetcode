# Automata 自动机

这里主要讨论**确定有限状态自动机**([deterministic finite automation (DFA)](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)), 这是一种数学模型，用于描述有限个状态之间的转移, 在DP问题中我们的state transition function就是一种自动机。

!!! info
    Finite State Machine (FSM)是最简单的一种自动机, DFA是FSM的一种特例.我们就学习这个问题就好了.

## 数学描述

一个自动机可以用一个五元组(tuple)来描述, where $M = \Sigma,\Gamma,\mathbb{Q},\delta,\lambda$

- $\Sigma$ 是输入字母表, 是一个有限的集合
- $\Gamma$ 是输出字母表, 是一个有限的集合
- $\mathbb{Q}$ 是状态集合.
- $\delta$: 状态转移函数(state transition function). $\Sigma \times \mathbb{Q} \rightarrow \mathbb{Q}$ 是, 将**状态输入Q**映射到后续状态. 可以理解为接受初始条件后，状态的不断自我更新。可以理解为数值计算中对于state variable的不断迭代更新，计算residual直到小于certain convergence criteria, 然后收敛.
- $\lambda$: 输出函数(output function). $\Sigma  \times \mathbb{Q} \rightarrow \Gamma$, 将**状态输入Q**映射到输出. 

如果$\mathbb{Q}$是有限的，那么$M$是一个有限自动机.

## 状态转移图(state transition diagram)



## Reference

- [cs standford](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/automata-theory/basics.html)
- [lumin article](https://www.lumin.tech/articles/automata-theory-basics/)
- [lingero article](https://lingeros-tot.github.io/introduction/)
- [OI wiki](https://oi-wiki.org/string/automaton/)