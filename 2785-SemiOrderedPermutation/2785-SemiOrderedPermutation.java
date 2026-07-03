// Last updated: 7/3/2026, 12:50:05 PM
class Solution {
    public int semiOrderedPermutation(int[] nums) {
        int min = -1, max = -1;
        int n = nums.length ;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) min = i;
            else if (nums[i] == n) max = i;

            // Early exit if both found
            if (min != -1 && max != -1) break;
        }
        if (max<min)
            return (n-(max)+min-2);
        else 
            return (min+n-max-1);
      
    }
}