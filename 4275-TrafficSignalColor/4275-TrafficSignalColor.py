# Last updated: 7/3/2026, 12:55:05 PM
class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0 :
            return "Green"
        elif timer ==30 :
            return "Orange"
        elif 30<timer and timer <=90 :
            return "Red"
        else:
            return "Invalid"