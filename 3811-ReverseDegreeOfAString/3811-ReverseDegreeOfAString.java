// Last updated: 7/3/2026, 12:49:04 PM
class Solution {
    public int reverseDegree(String s) {
        int count = 0 ;
        int index = 1 ;
        for (char i : s.toCharArray() ){
            int fake = i ;
            count += (123-fake)*index;
            index++;
        }


        return count ;
    }
}