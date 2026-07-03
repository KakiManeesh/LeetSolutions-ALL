# Last updated: 7/3/2026, 1:01:45 PM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_length = 0

        for i in sentences :
            
            max_length = max( max_length , len(i.split()) )
        return max_length