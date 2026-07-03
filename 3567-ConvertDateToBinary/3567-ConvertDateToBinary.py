# Last updated: 7/3/2026, 12:49:17 PM
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        a = bin(int(date[:4]))[2:] +"-"+ bin(int(date[5:7]))[2:] + "-" + bin(int(date[8:]))[2:]
        return a