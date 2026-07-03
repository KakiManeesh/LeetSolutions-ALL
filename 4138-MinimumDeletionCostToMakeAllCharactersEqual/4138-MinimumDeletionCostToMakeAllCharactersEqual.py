# Last updated: 7/3/2026, 12:55:19 PM
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        unique_ = list(set(s))
        
        cost_each = [0] * len(unique_)
        
        for i in range(len(s)):
            cost_each[unique_.index(s[i])] += cost[i]
        
        total_cost = sum(cost)
        min_value = float('inf')
        
        for i in cost_each:
            min_value = min(min_value, total_cost - i)
        
        return min_value
