class Solution:
    def twoStrCommonPrefix(self,s,t):
        # s: input string 1
        # t: input string 2
        # res [str]: common prefix between two strings
        res = ""

        # determine the min length between two characters
        min_length = min(len(s),len(t))

        # iterate the smaller string
        for i in range(min_length):
            # 判断俩字符是否相等
            if s[i] == t[i]:
                # 相等则累加入res
                res += s[i]
            else:
                # 不相等直接return res为common prefix 
                return res
        
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # horizontal scanning appraoch

        # edge cases
        if len(strs) == 0:
            return ""


        res = strs[0]
        for i in range(len(strs)-1):
            # 比较俩相邻的string
            res = self.twoStrCommonPrefix(res,strs[i+1])

        
        return res
