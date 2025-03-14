''' Dynamic Programming (Tabulation - Bottom-Up)'''

class Solution:
    def count(self, coins, sum):
        # Initialize DP array with size (sum + 1), all set to 0
        dp = [0] * (sum + 1)
        
        # Base case: One way to make sum 0 (by taking no coins)
        dp[0] = 1

        # Iterate over each coin
        for coin in coins:
            for j in range(coin, sum + 1):
                dp[j] += dp[j - coin]

        return dp[sum]



'''
Recursion + Memoization(Top-Down DP) 
💡 Idea
1️⃣ At each step, we either include or exclude the current coin. 
2️⃣ Recursive Formula:
count(i, sum) = count(i - 1, sum) + count(i, sum - coins[i])
3️⃣ Use memoization to store results and avoid recomputation.
'''
class Solution:
    def count(self, coins, sum):
        # Memoization dictionary
        memo = {}

        def helper(i, remaining_sum):
            # Base cases
            if remaining_sum == 0:
                return 1  # Found a valid way
            if i >= len(coins) or remaining_sum < 0:
                return 0  # Invalid case
            
            # Check if result is already computed
            if (i, remaining_sum) in memo:
                return memo[(i, remaining_sum)]

            # Either take the current coin (stay at i) or skip it (move to i+1)
            take = helper(i, remaining_sum - coins[i])
            skip = helper(i + 1, remaining_sum)

            # Store result in memo and return
            memo[(i, remaining_sum)] = take + skip
            return memo[(i, remaining_sum)]

        return helper(0, sum)


'''
🔹 What’s Memoization?
Instead of recomputing results, we store them in a dictionary (hash map) and reuse them. This prevents redundant calculations and makes recursion super efficient! 

Memoization is a technique where we store previously computed results to avoid redundant calculations. It’s like having a cheat sheet 📝 for subproblems, so we don’t have to solve them again and again! 🚀
✅ Speeds up recursion by remembering solutions to already-solved subproblems.
✅ Reduces time complexity from exponential to polynomial in many cases.
'''
