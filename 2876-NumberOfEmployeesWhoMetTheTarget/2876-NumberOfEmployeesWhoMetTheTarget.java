// Last updated: 7/3/2026, 12:50:02 PM
class Solution {
  public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
    return (int) Arrays.stream(hours).filter(hour -> hour >= target).count();
  }
}