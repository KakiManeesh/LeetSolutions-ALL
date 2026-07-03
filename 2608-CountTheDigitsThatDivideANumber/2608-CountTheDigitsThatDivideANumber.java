// Last updated: 7/3/2026, 12:50:20 PM
class Solution {
    public int countDigits(int num) {
        int num1 = num ;
        int count = 0;
        while (num1 > 0 ){
            if (num%(num1%10) == 0 )
                count ++ ;
            num1 = num1 /10 ;
        }
        return count ;
        
    }
}