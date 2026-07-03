// Last updated: 7/3/2026, 1:31:46 PM
class Solution {
    public int[] buildArray(int[] nums) {
        int[] ans = new int[nums.length];
        int i = 0 ;
        while ( i < nums.length  ){
            ans[i] = nums[nums[i]];
            ++i;
        }
        return ans ;

    }
}