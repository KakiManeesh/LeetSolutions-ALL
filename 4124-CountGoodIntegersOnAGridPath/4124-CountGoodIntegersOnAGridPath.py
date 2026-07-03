# Last updated: 7/3/2026, 12:55:21 PM
class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        # Calculate which positions in the 16-digit number are visited
        path_positions = []
        row, col = 0, 0
        path_positions.append(row * 4 + col)
        
        for direction in directions:
            if direction == 'D':
                row += 1
            else:  # 'R'
                col += 1
            path_positions.append(row * 4 + col)
        
        # path_positions: which indices in the 16-digit string form the path
        
        def count_good(num):
            """Count good numbers from 0 to num (inclusive)"""
            s = str(num).zfill(16)
            memo = {}
            
            def dp(pos, tight, last_digit, path_idx):
                # pos: current position in 16-digit string (0-15)
                # tight: whether still bounded by upper limit
                # last_digit: last digit in the path sequence
                # path_idx: which position in path we're at (0-6)
                
                if path_idx == 7:
                    # Completed path with non-decreasing sequence
                    return 1
                
                if pos == 16:
                    return 0
                
                if (pos, tight, last_digit, path_idx) in memo:
                    return memo[(pos, tight, last_digit, path_idx)]
                
                limit = int(s[pos]) if tight else 9
                result = 0
                
                if pos == path_positions[path_idx]:
                    # Current position is next position in path
                    # Digit must be >= last_digit
                    for digit in range(last_digit, limit + 1):
                        new_tight = tight and (digit == limit)
                        result += dp(pos + 1, new_tight, digit, path_idx + 1)
                else:
                    # Current position is NOT in path
                    # Can be any digit, don't advance path_idx
                    for digit in range(0, limit + 1):
                        new_tight = tight and (digit == limit)
                        result += dp(pos + 1, new_tight, last_digit, path_idx)
                
                memo[(pos, tight, last_digit, path_idx)] = result
                return result
            
            return dp(0, True, 0, 0)
        
        # Count from l to r = count(0 to r) - count(0 to l-1)
        return count_good(r) - count_good(l - 1)