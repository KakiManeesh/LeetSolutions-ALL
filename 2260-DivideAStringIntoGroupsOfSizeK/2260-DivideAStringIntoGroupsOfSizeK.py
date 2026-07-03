# Last updated: 7/3/2026, 1:01:38 PM
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        out = [s[i:i+k]  for i in range(0,len(s),k)]
        
        if len(s)%k!=0 :
            out[-1] = out[-1] + fill*(k-len(s)%k)
        return out