// Last updated: 7/3/2026, 12:49:43 PM
class Solution {
  public String triangleType(int[] nums) {
    Arrays.sort(nums);
    if (nums[0] + nums[1] <= nums[2])
      return "none";
    if (nums[0] == nums[1] && nums[1] == nums[2])
      return "equilateral";
    if (nums[0] == nums[1] || nums[1] == nums[2])
      return "isosceles";
    return "scalene";
  }
}