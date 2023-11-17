class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # brute force would go through every single pair in the array, O(n^2)
        # DP[j]: the maximum score you could get for the pair where it's (nums[i], nums[j])

        if len(values) == 2: return values[1] + values[0] + 0 - 1

        # intiialze DP wizhe zeros
        DP = [0 for _ in range(len(values))]

        # find the prefix i that will give us highest score.
        best_prefix_i = 0
       

        for j in range(1,len(values)):
            if values[j-1] + j-1 >= values[best_prefix_i] + best_prefix_i:
                best_prefix_i = j-1
            DP[j] = best_prefix_i + values[best_prefix_i] + values[j] - j
        
        return max(DP)