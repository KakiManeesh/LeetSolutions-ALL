// Last updated: 7/3/2026, 12:50:16 PM
class Solution {
    public int differenceOfSum(int[] nums) {
        int totalSum = 0; // To hold the total sum of the numbers
        int digitSum = 0; // To hold the sum of the digits of all numbers

        for (int num : nums) {
            totalSum += num; // Add the current number to the total sum
            digitSum += getDigitSum(num); // Add the sum of digits of the current number
        }

        return totalSum - digitSum; // Return the difference
    }

    private int getDigitSum(int num) {
        int sum = 0;
        // Using do-while to handle the case when num is 0
        do {
            sum += num % 10; // Add the last digit to sum
            num /= 10;        // Remove the last digit
        } while (num > 0);
        
        return sum; // Return the sum of digits
    }
}
