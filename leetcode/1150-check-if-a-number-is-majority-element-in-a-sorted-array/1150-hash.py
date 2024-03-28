class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # 出现超过一半的次数，那就是majority elements
        # Intuition: hash for frequency count

        
        
        numFrequencyHash = {}
        targetFlag = False

        for num in nums:
            # edge case, whether target in List
            if num == target:
                targetFlag = True

            # general case
            if num not in numFrequencyHash.keys():
                numFrequencyHash[num] = 1
            else:
                numFrequencyHash[num] += 1

        # 判断target是否存在在数组里;
        if targetFlag == False:
            return False
        else:
            return numFrequencyHash[target] > len(nums)//2 
    
