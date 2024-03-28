class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scan Solution
        
        # if no common prefix, then ""
        res = ""

        # iterate i time where i equals number of chars in the str
        # i 为比较第几个character
        for i in range(len(strs[0])):
            # traverse str
            for str in strs:
                # 判断是否index out of range OR 不相等
                if i == len(str) or str[i] != strs[0][i]:
                    return res
            
            # 累加入string
            res += strs[0][i]

        return res