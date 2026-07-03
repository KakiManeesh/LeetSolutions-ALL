// Last updated: 7/3/2026, 12:49:31 PM
class Solution {
    public boolean isArraySpecial(int[] nums) {
        if (nums.length == 1)
            return true;
        
        int i = 0 ;

        while (i < nums.length -1 ){
            if ( (nums[i]+nums[i+1])%2 == 0  ){
                return false;
            }
            i++;
        }
        return true ;
        
    }
}