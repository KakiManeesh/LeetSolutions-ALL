# Last updated: 7/3/2026, 1:01:16 PM
class Solution:
    def countTime(self, time: str) -> int:
        answer = 1
        if time[3] =='?': 
            answer *= 6
        if time[4] == '?':
            answer *= 10
        
        if time[0] == '?' and time[1] != '?' and int(time[1]) <4:
            return answer * 3
        
        if time[0]== '?' and time[1] != '?':
            return answer * 2



        if time[0] == '?' and time[1] == '?' :
            return answer * 24
        


        if time[0] != '?' and int(time[0]) < 2 and time[1] == '?':
            return answer * 10
        
        if time[0] != '?' and int(time[0]) == 2 and time[1] == '?':
            return answer * 4

        return answer