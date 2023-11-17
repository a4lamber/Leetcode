---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Intuition
这题转化一下题意:
- 将所有的odd nodes组成一个链表A
- 将所有的even nodes组成一个链表B
- 连接A的尾巴和B的头

Technique:
- two pointers, odd and even; even pointer is ahead of odd pointer, so we use that in the `while`
- corner cases, it has zero or it has one node;


