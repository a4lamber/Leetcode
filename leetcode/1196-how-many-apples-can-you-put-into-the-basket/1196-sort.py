class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        # sort it, O(nlogn)
        weight.sort()

        appleCounter = 0
        totalAppleWeight = 0

        # traverse, O(n)
        for singleAppleWeight in weight:
            if totalAppleWeight + singleAppleWeight > 5000:
                break
            
            appleCounter += 1
            totalAppleWeight += singleAppleWeight

        return appleCounter




