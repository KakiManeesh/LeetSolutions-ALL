# Last updated: 7/3/2026, 12:55:12 PM
import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:       
        a,b,c = tuple(sides)

        if a + b <= c or  a + c <= b or  b + c <= a :
            return []
        
        s = (a**2) + (b**2) + (c**2)

        output = []

        A = math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c)))
        B = math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))
        C = math.degrees(math.acos((a*a + b*b - c*c) / (2*a*b)))
        output = [A,B,C]
        output.sort()
        return output