# Last updated: 7/3/2026, 1:01:52 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        fake  = "".join(operations)

        return (fake.count('+')-fake.count('-'))//2 