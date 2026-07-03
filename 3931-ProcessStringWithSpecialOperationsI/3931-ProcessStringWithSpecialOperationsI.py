# Last updated: 7/3/2026, 12:49:00 PM
class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if 'a' <= ch <= 'z':
                res.append(ch)

            elif ch == '*':
                if res:
                    res.pop()

            elif ch == '#':
                res.extend(res)

            else:  # ch == '%'
                res.reverse()

        return "".join(res)