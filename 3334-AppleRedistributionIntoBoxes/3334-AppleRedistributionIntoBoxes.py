# Last updated: 7/3/2026, 12:49:39 PM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        total = sum(apple)
        capacity.sort(reverse =True)
        count = 0
        for i in capacity :
            if total > 0 :
                count+=1
                total -= i
            else:
                return count
        

        return len(capacity)