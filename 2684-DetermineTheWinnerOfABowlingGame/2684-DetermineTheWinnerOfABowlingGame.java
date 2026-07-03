// Last updated: 7/3/2026, 12:50:13 PM
class Solution {
    public int isWinner(int[] player1, int[] player2) {

        int n = player1.length; 
        int score1 = 0, score2 = 0; 
        int check1 = 0, check2 = 0;

        for (int i = 0; i < n; i++) {
            
            if (check1 != 0) {
                score1 += player1[i] * 2;    
                check1 -= 1;           
            } else {
                score1 += player1[i];
            }

            if (check2 != 0) {
                score2 += player2[i] * 2; // Changed to score2 += player2[i] * 2;
                check2 -= 1; // Changed decrement from 2 to 1
            } else {
                score2 += player2[i];
            }

            if (player1[i] == 10) {
                check1 = 2; // Set check1 to 2 when player1 scores 10
            }
            if (player2[i] == 10) {
                check2 = 2; // Set check2 to 2 when player2 scores 10
            }
        }

        if (score1 > score2) {
            return 1;
        }
        if (score2 > score1) {
            return 2;
        }
        return 0;  
    }
}
