// Last updated: 7/3/2026, 12:49:22 PM
class Solution {
    public boolean canAliceWin(int[] nums) {
        int a = 0;
        for (int i : nums){
            if (i > 9 )
                a+=i;
            else
                a-=i;
        }
        return (a!=0);
        
    }
}