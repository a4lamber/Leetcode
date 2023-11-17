class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # hash Solution, O(n) in time, O(n) in space

        hashTable1 = set(arr1)
        hashTable2 = set(arr2)
        hashTable3 = set(arr3)

        # travere one hash
        res = []

        for val in hashTable1:
            if val in hashTable2 and val in hashTable3:
                res.append(val)
        
        return sorted(res)
        


                






