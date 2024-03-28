class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for item1 in arr1:
            counter = 0
            for item2 in arr2:
                if abs(item1 - item2) <= d:
                    counter +=1
            if counter == 0: res += 1
        return res
