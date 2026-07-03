# Last updated: 7/3/2026, 12:49:13 PM
def shift_string(s):
    result = ''
    for ch in s:
        if ch == 'z':
            result += 'a'
        else:
            result += chr(ord(ch) + 1)
    return result

class Solution:
    
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s)<k :
            s = s +shift_string(s)
        return s[k-1]       