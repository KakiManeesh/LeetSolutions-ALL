// Last updated: 7/3/2026, 12:49:57 PM
class Solution {
    public int countPairs(List<Integer> nums, int target) {

        int n = nums.size() ;
        int i = 0 ;
        int count = 0 ;
        while (i<(n-1)){
            
            int j = i+1 ;
            while( j < n ){
                if ((nums.get(i) + nums.get(j) ) < target) {
                    count ++ ;
                }
                j++;
            }
            i++;
        }
        return count ;
        
    }
}