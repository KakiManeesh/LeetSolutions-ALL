# Last updated: 7/3/2026, 12:50:07 PM
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if len(prices) in (0,1) :
            return money
        
        a = min(prices)
        prices.remove(a)
        b = min(prices)
        
        if ( money >= a+b ):
            return money - a - b 
        return money