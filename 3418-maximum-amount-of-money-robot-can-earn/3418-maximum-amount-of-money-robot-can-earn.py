class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        '''
            [0,1,-1],
            [1,-2,3],
            [2,-3,4]

            [] m  * n * k grid

            OG
            [0,1,-1],
            [1,-2,3],
            [2,-3,4]

            DP k = 0
            [0, 1, 0]
            [1, -1, 3]
            [3, 0, 7]
            
            DP k = 1

            dp[i][j][k] = max( 
                                dp[i - 1][j][k] + coin[i][j],
                                dp[i][j - 1][k] + coin[i][j],
                                dp[i - 1][j][k - 1],
                                dp[i][j - 1][k - 1]
                            )
        '''

        m = len(coins)
        n = len(coins[0])

        dp = [[float('-inf')] * 3 for _ in range(n)]

        dp[0][0] = coins[0][0]

        for k in range(1, 3):
            dp[0][k] = max(coins[0][0], 0)

        for j in range(1, n):
            dp[j][0] = dp[j - 1][0] + coins[0][j]
            for k in range(1, 3):
                dp[j][k] = max(
                    dp[j - 1][k] + coins[0][j],
                    dp[j - 1][k - 1]
                )

        for i in range(1, m):
            curr = [[float("-inf")] * 3 for _ in range(n)]
            curr[0][0] = dp[0][0] + coins[i][0]

            for k in range(1, 3):
                curr[0][k] = max(
                    dp[0][k] + coins[i][0],
                    dp[0][k - 1]
                )


            for j in range(1, n):
                curr[j][0] = max(
                    curr[j - 1][0] + coins[i][j],
                    dp[j][0] + coins[i][j],
                )

                for k in range(1, 3):
                    curr[j][k] = max(
                        curr[j - 1][k] + coins[i][j],
                        dp[j][k] + coins[i][j],
                        curr[j - 1][k - 1],
                        dp[j][k - 1]
                    )
            dp = curr

        return dp[n - 1][2]
