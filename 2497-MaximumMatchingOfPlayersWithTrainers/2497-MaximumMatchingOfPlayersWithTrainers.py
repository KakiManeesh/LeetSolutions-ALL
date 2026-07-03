# Last updated: 7/3/2026, 1:01:19 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i,j,count,m,n = 0,0,0,len(players),len(trainers)

        players.sort()
        trainers.sort()

        while ( i<m and j<n ):
            if players[i] <= trainers[j]:
                count +=1 
                i+=1
                j+=1
            else:
                j+=1
        return count