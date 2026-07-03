// Last updated: 7/3/2026, 1:01:44 PM
class Solution {
    public String firstPalindrome(String[] words) {
        for (String s : words) {
            if (isPalindrome(s)) return s;
        }
        return "";
    }

    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false; // Not a palindrome
            }
            left++;
            right--;
        }
        return true; // Is a palindrome
    }
}
