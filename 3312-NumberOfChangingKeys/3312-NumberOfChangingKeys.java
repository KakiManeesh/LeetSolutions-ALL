// Last updated: 7/3/2026, 12:49:44 PM
class Solution {
    public int countKeyChanges(String s) {
        int change = 0;
        char current = s.charAt(0);

        for (char i : s.toCharArray()) {
            if (current != i && current != Character.toLowerCase(i) && current != Character.toUpperCase(i)) {
                change++;
                current = i;
            }
        }
        return change;
    }
}
