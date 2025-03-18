class Solution:
    def equalPartition(self, arr):
        total_sum = sum(arr)
        
        # If total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(arr)
        
        # DP table
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Base case: Sum 0 can always be formed
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]
