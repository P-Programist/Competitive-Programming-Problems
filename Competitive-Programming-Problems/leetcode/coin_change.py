# Summary: Given a list of coin denominations and an amount, find the fewest number of coins needed to make up that amount.

# Approach:
#     Dynamic programming approach: dp[i] = fewest coins to reach amount i. Initialize dp[0] = 0.

# Complexity:
#     Time: O(n * amount)
#     Space: O(amount)


def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
