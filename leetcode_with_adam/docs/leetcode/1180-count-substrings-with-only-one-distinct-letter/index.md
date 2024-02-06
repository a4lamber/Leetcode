---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---


# 原来思路
我最先的思路是:
- 先根据string, change of variable为条件，split into substrings, 然后append到一个list
- 然后分别求等加数列

但可以两步并一步



## 改善逻辑

关于boundary总是搞不清楚，思路都是对的, 现在知道了，对于out of index这种判定条件的几个trick

- 直接traverse right指针, 而不是用`while`写那么多判定
- `for right in range(len(s)+1)`, 多一个index
- `if right == len(s) or s[left] != s[right]` 由于python执行expression是只要前面的pass了，然后就不检查后面了, 为了避免index out of range error, 只能这么做;





