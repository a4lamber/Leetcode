class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def oneWayMapping(str1,str2):
            stringHash = {}
            # traverse the string and initialize the hash        
            for i in range(len(s)):
                # check if collision happens
                if str1[i] in stringHash:
                    if stringHash[str1[i]] != str2[i]:
                        return False
                # build the mapping
                stringHash[str1[i]] = str2[i]
            return True
        
        return oneWayMapping(s,t) and oneWayMapping(t,s)
