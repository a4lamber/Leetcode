class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # brute force would go through every single pair in the array, O(n^2)

        if len(values) == 2: return values[1] + values[0] + 0 - 1

        # find the prefix i that will give us highest score.
        best_prefix_i = 0
        global_max = 0

        for j in range(1,len(values)):
            if values[j-1] + j-1 >= values[best_prefix_i] + best_prefix_i:
                best_prefix_i = j-1
            curr_max = best_prefix_i + values[best_prefix_i] + values[j] - j
            if curr_max > global_max: global_max = curr_max

        return global_max