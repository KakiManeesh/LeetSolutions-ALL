// Last updated: 7/3/2026, 12:49:38 PM
class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {

        int drank = numBottles ; 

        if (numBottles < numExchange)
            return numBottles ;

        
        while (numBottles >= numExchange){
            
            numBottles -= numExchange ;
            numExchange ++ ;
            drank ++ ;
            numBottles++ ;

        }
        return drank;
    }
}