---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
思路只想到brute force, 还用到了auxillary data structure `list()`, 优化思路是one-pass solution, 由于你只感兴趣最短距离，你只需要traverse one time, 每一次都update最新的match word的信息，这样的话你每次比较的都是距离最近的两个matches的距离，就缩小了search space;

# Approach
<!-- Describe your approach to solving the problem. -->
- 设置三个int `i`,`j` for word in wordsDict match word1 and word2's index, respectively. `minimumLength` for minimum length
- traverse the array once 然后分别判断和update你match word1 and word2的信息;
- 比较;

# Complexity
- Time complexity: O(nm), n is the length of the Array, m is the total length of the String word1 and word2 (由于需要比较来着)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```java
class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        // one pass Solution
        // traverse the soluton one time only
        int i = -1;
        int j = -1;
        int minimumLength = wordsDict.length;

        for (int index = 0; index < wordsDict.length; index++) {
            // mark occurence of word1
            if (wordsDict[index].equals(word1)) {
                i = index;
            }
            
            // mark occurence
            if (wordsDict[index].equals(word2)) {
                j = index;
            }
            
            //always comparing the closest occurence of both words
            if (i != -1 && j != -1){
                // emulate math.abs()
                int currentLength = i - j;
                if (currentLength < 0) {
                    currentLength *= -1;
                }

                // update current length
                if (currentLength < minimumLength) {
                    minimumLength = currentLength;
                }

                // optimization, no need to go further if minimumLength is one
                if (minimumLength == 1) {
                    return minimumLength;
                }
            }
        }


        return minimumLength;
    }
}
```

> Follow-up: what about max distance? how to decrease search space