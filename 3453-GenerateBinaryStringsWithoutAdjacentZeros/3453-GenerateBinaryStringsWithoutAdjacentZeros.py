# Last updated: 7/3/2026, 12:49:27 PM
class Solution:
    def validStrings(self, n: int) -> List[str]:
        output = []
        options = ['1','0']
        def soln( curr):
            if len(curr) == n :
                output.append(curr)
                return
            
            if not curr or curr[-1] !='0' :
                soln( curr + '0'  )
            soln( curr+ '1')
            
        
        soln("")
        return output