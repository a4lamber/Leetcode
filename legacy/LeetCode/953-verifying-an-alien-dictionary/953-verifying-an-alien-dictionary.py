class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_map = {}
        for index,char in enumerate(order):
            order_map[char] = index

        # iterate through the list
        for i in range(len(words)-1):
            # iterate throught the 1st string in the string pair
            for j in range(len(words[i])):
                

                # 如果坚持到这,还没分出大小, 比较string长度
                # ["apple","app"]
                if j >= len(words[i+1]):
                    return False
                
                # 找到俩相邻string的第一个不同的character
                if words[i][j] != words[i+1][j]:
                    # 比较char in string one 是否大于char in string two
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    
                    # not sorted, 比较下两个string去
                    break
                """
                三种方式跳出内循环:
                1. 比较current index j with 下一个string的长度，cover corner cases ["apple","app"]
                if j >= len(words[i+1])
                2. 第一个不相同的char, 满足sorted, then break
                3. 第一个不相同的char,不满足sorted, return False
                那么不跳出内循环的可能性，就是:
                ["app","apple"] 满足app < apple, sorted;
                """
                

        return True

