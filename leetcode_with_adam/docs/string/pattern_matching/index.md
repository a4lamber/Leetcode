# String Pattern Matching

> Pattern Matching (模式匹配): 给定字符串$S$和$T$, 在主串$S$中找到模式串$T$的位置. 

根据类型，可以分为

- `单串匹配`: 只有一个pattern string和一个主串，找出前者在后者中的所有位置。
- `多串匹配`: 有多个pattern string和一个主串，找出每个pattern string在主串中的位置。
    - 可以直接用`单串匹配`的方法，一个一个找，但效率很低。
- `其他类型`: 匹配串的任意后缀，或者匹配多个串的任意后缀。
    - 这种算是`partial string pattern matching`了，partial string其实也就是substring, prefix is substring starting from index `0`, suffix is substring ending at index `n-1`.


## string pattern matching 应用

pattern matching几乎是所有字符串处理的基础，因此有很多应用场景，比如：

- command + F: 搜索你想要的文字,在IDE, browser etc

