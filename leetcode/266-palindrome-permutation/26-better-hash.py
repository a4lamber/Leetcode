class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 之前的思路:
        # 两种conditions是palindrom的条件:
        # odd number of string, 其中有一个x%2 == 1, 剩下的都满足y%2 == 0
        # even number of string, 那么每个item都满足y%%2 == 0:

        # 利用这个思路，再和valid parathensis中的思路结合一下
        # 奇数和偶数这两个条件的中和条件就是，满足只有一个单身汉,剩下都是情侣

        unpaired = set()

        for char in s:
            if char not in unpaired:
                # 没找到pair, 先去里面等着吧
                unpaired.add(char)
            else:
                # 满足一个pair, 消消乐
                unpaired.remove(char)


        return len(unpaired) <= 1
