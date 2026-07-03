// Last updated: 7/3/2026, 12:49:19 PM
class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int v = 0, h = 0;

        for (String command : commands) {
            switch (command) {
                case "UP": v--; break;
                case "DOWN": v++; break;
                case "LEFT": h--; break;
                case "RIGHT": h++; break;
            }
        }
        return (v * n + h);
    }
}
