# Last updated: 7/3/2026, 1:01:14 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15 , celsius*1.80 +32.00]
        