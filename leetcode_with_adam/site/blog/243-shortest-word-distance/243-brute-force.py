class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # brute force (without list)
        
        minimumDistance = len(wordsDict)

        # check every possbility O(n**2)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2 and abs(i-j) < minimumDistance:
                        minimumDistance = abs(i-j)

        return minimumDistance


            