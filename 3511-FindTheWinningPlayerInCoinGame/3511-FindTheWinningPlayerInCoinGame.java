// Last updated: 7/3/2026, 12:49:23 PM
class Solution {
    public String losingPlayer(int x, int y) {

        boolean turn = true ;

        while ( x>=1 && y>=4 ){

            x-=1 ;
            y-=4 ;
            
            turn = ! turn ;
        }
        if (!turn){
            return "Alice";
        }
        else{
            return "Bob";
        }
        
    }
}