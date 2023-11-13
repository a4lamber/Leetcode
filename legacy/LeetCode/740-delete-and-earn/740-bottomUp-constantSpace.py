class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # edge case

        # aggregate points into a bin
        # nums :  total points = nums * count
        pointsBasket = {}
        for num in nums:
            if num not in pointsBasket:
                pointsBasket[num] = num
            else:
                pointsBasket[num] += num
        
        
        houses = list(set(nums))
        houses.sort()
        
        if len(houses) == 1: return pointsBasket[houses[0]]


        # DP[i]: current maximum points for subarray ending on houses[i] (don't have to include houses[i])
        prevPrev = pointsBasket[houses[0]]
        if houses[1] - houses[0] > 1:
            prev = prevPrev + pointsBasket[houses[1]]
        else:
            prev = max(pointsBasket[houses[0]],pointsBasket[houses[1]])

        for i in range(2,len(houses)):
            temp = prev

            if houses[i] - houses[i-1] > 1:
                prev = prev + pointsBasket[houses[i]]
            else:
                prev = max(prev, prevPrev + pointsBasket[houses[i]])

            prevPrev = temp

        return prev


