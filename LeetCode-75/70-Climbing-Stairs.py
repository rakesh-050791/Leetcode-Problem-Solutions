# 70. Climbing Stairs | #Easy #DP

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.calculateWays(n, dp)
    
    def calculateWays(self, i, dp):
        if i <= 1:
            dp[i] = 1

        if dp[i] == -1:
            dp[i] = self.calculateWays(i-1, dp) + self.calculateWays(i-2, dp)

        return dp[i]