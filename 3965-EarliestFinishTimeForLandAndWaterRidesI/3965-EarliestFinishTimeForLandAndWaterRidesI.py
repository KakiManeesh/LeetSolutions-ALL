# Last updated: 7/3/2026, 12:55:32 PM
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        land = [ [landStartTime[i] ,landDuration[i] , landDuration[i]+landStartTime[i] ] for i in range(len(landStartTime)) ]

        water = [ [waterStartTime[i] ,waterDuration[i] , waterDuration[i]+waterStartTime[i] ] for i in range(len(waterStartTime)) ]

        # if i take the land first
        def land_water():
            temp1 = land.copy()
            temp1.sort(key = lambda x : x[2] )
            end  = temp1[0][2]
            min_ = float('inf')
            for i in water :
                if i[0] > end :
                    min_ = min(min_,i[0] - end + i[1])
                else:
                    min_ = min( min_ , i[1] )
            
            return end + min_ 
        
        def water_land():
            temp1 = water.copy()
            temp1.sort(key = lambda x : x[2] )
            end  = temp1[0][2]
            min_ = float('inf')
            for i in land :
                if i[0] > end :
                    min_ = min(min_,i[0] - end + i[1])
                else:
                    min_ = min( min_ , i[1] )
            
            return end + min_ 

        return min(land_water(),water_land())
        