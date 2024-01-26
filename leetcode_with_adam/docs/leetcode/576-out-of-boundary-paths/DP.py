from collections import defaultdict


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        # m,n: grid size; startRow, startColumn: initial position; maxMove: <= maxMove
        # DP[i][j]: number of ways to reach position i, j for x moves, where x <= maxMove
        # state transition function:(excluding boundary nodes)
        # DP[i][j] = DP[i-1][j]
        #          + DP[i][j-1]
        #          + DP[i+1][j]
        #          + DP[i][j+1]
        # 1. traverse num of moves allowed x , where 0 <= x <= maxMove
        # 2. By traverse the 2d array, update the DP[i][j] at x based on info in the DP[i][j] at x - 1. You can think of it as temporal evolution

        # DP_last_step = [[0 for _ in range(n)] for _ in range(m)]
        # DP = [[0 for _ in range(n)] for _ in range(m)]

        # # initialization
        # DP[startRow][startColumn] = 1
        # DP_last_step[startRow][startColumn] = 1

        DP = defaultdict(lambda: 0)
        DP_last = defaultdict(lambda: 0)

        # initialization
        DP[(startRow, startColumn)] = 1
        DP_last[(startRow, startColumn)] = 1

        res = 0
        for t in range(maxMove):
            for i in range(m):
                for j in range(n):
                    # max points to get is four when m = 1, n = 1, starting at (0,0)
                    points = 0
                    if i + 1 >= m:
                        points += 1
                    if i - 1 < 0:
                        points += 1
                    if j - 1 < 0:
                        points += 1
                    if j + 1 >= n:
                        points += 1
                    res += DP[(i, j)] * points

                    # update DP at t based on t-1
                    DP[(i, j)] = (
                        DP_last[(i - 1, j)]
                        + DP_last[(i, j - 1)]
                        + DP_last[(i + 1, j)]
                        + DP_last[(i, j + 1)]
                    )

            # update DP_last with DP
            DP_last = DP.copy()

        return res % (10**9 + 7)
