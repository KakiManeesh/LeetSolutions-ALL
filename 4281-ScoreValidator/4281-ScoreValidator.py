# Last updated: 7/3/2026, 12:54:58 PM
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for i in events :
            if counter == 10 :
                break
            if i == "W" :
                counter += 1
            elif i == "WD" :
                score += 1
            elif i == "NB" :
                score += 1
            else :
                score += int(i)

        return [score, counter]