class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # constant space
        # return integer array of length 2

        # left and right pointers
        left = 0
        right = len(numbers) - 1

        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                # need to decrease it
                right -= 1
            else:
                left += 1
                

        

                
            



