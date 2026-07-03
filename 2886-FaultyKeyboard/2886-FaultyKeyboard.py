# Last updated: 7/3/2026, 12:50:01 PM
class Solution:
    def finalString(self, s: str) -> str:
        a = []
        reverse = False
        for char in s:
            if char == 'i':
                reverse = not reverse
            else:
                if reverse:
                    a.insert(0, char)  # Add to the front in reverse mode
                else:
                    a.append(char)  # Append normally
        return "".join(a[::-1] if reverse else a)
