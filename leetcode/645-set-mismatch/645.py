class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # BF solution: traverse and record in hashmap to find duplicate
        # use len(nums) same as s, traverse this
        # [1,2,2,4] -> [2,3]
        # 1. Construct an auxillary hashmap to store occurence as value, default to 1
        # 2. traverse nums to find minus the occurence, missing will be 1 and duplicate will be -1, else 0.
        # O(n) in both space and time
        hashmap = dict()
        for i in range(1, len(nums) + 1):
            hashmap[i] = 1

        for num in nums:
            hashmap[num] -= 1

        for i, occurence in hashmap.items():
            if occurence == -1:
                occur_twice = i

            if occurence == 1:
                missing = i

        return [occur_twice, missing]
