// Last updated: 7/3/2026, 12:49:48 PM
import java.util.Arrays;

class Solution {
    public int[] numberGame(int[] nums) {
        
        Arrays.sort(nums);
        
        for (int i = 0; i<nums.length ;i+=2){
            int temp = nums[i];         // Store nums[i] in a temporary variable
            nums[i] = nums[i + 1];     // Assign nums[i + 1] to nums[i]
            nums[i + 1] = temp; 
        }

        return nums;
    }
}
