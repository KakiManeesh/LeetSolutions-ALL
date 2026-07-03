# Last updated: 7/3/2026, 12:49:11 PM
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        gain = [0] * n

        for i in range(n):
            fi = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    gain[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            cost = items[i][1]
            value = 1 + gain[i]

            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + value)

        min_price = min(price for _, price in items)

        ans = 0

        for spent in range(budget + 1):
            rem = budget - spent

            ans = max(
                ans,
                dp[spent] + rem // min_price
            )

        return ans