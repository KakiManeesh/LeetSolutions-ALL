// Last updated: 7/3/2026, 12:49:14 PM
import java.util.* ;
class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        
        List<Integer> give = new ArrayList<>() ;

        for (int i = 1 ;i<height.length ;i++){
            if (height[i-1] > threshold )
                give.add(i);
        }
        
        return give  ;
    }
}