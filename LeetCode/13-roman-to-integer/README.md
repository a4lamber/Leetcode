# Readme

## Approach 1: Brute force

### Intuition

Roman to Integer这一题, 第一次接触罗马数字时，是小时候玩真三国无双4时候，就知道真三国无双IV. 
由此知道罗马数字, 如下
|Symbol|Value|
|-|-|
|I|1|
|V|5|
|X|10|
|L|50|
|C|100|
|D|500|
|M|1000|

除此之外，将罗马数字的几个特殊用法，总结归纳如下
|Symbol|Value|
|-|-|
|IV|4|
|IX|9|
|XL|40|
|XC|90|
|CD|400|
|CM|900|

这样的话，这道题就可以设计成三步
- 设立两个hash table, 一个存表1，另一个存表2
- 循环，先检索是否存在特殊用法,如IV等，一旦找到将first occurence of certain key替换为`""`,如下`string.replace("IV","",1)`
- 循环检索是否存在其它常数项直到为结束


代码如下,
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # declare of output integer
        output = 0
        # declare of two hashmap
        hashmap_basic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        hashmap_derived = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        # better use while
        for item in hashmap_derived.keys():
            # check if any key in it
            if item in s:
                output += hashmap_derived[item]
                s = s.replace(item,"",1)

        # check basic dictionary
        while s is not '':
            for item in hashmap_basic.keys():
                if item in s:
                    output += hashmap_basic[item]
                    s = s.replace(item,"",1)
        
        return output
```

复杂度来说，空间复杂度为$O(1)$, 时间复杂度

## Approach 2: brute force 简单优化

> jerry提示我，第二步中for loop nested in while loop是很多余的，而且`s.replace()` 在python中计算也比较慢, 可以直接iterate string.

由此更改代码如下:

```Python
class Solution:
    def romanToInt(self, s: str) -> int:
        # declare of output integer
        output = 0
        # declare of two hashmap
        hashmap_basic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        hashmap_derived = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        # better use while
        for item in hashmap_derived.keys():
            # check if any key in it
            if item in s:
                output += hashmap_derived[item]
                s = s.replace(item,"",1)

        # 由于不存在特例了，直接iterate string就好
        for c in s:
            output += hashmap_basic[c]

        return output

```