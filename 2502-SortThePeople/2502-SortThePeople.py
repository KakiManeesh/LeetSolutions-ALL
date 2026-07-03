# Last updated: 7/3/2026, 1:01:18 PM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        k = [[names[i],heights[i]] for i in range(len(heights)) ]
        k.sort(key = lambda x :-x[1])

        return [i[0] for i in k]