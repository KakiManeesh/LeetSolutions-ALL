# Last updated: 7/3/2026, 12:54:56 PM
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        from collections import deque
        
        # Initialize grid
        grid = [[0] * m for _ in range(n)]
        
        # Initialize queue and grid with sources
        queue = deque()
        for r, c, color in sources:
            grid[r][c] = color
            queue.append((r, c, color))
        
        # BFS - process level by level
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            # Process current level (all cells at same distance)
            next_cells = {}  # (r, c) -> color
            
            # Process all cells at current level
            for _ in range(len(queue)):
                r, c, color = queue.popleft()
                
                # Spread to adjacent uncolored cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check bounds
                    if 0 <= nr < n and 0 <= nc < m:
                        # If uncolored, try to color it
                        if grid[nr][nc] == 0:
                            if (nr, nc) not in next_cells:
                                next_cells[(nr, nc)] = color
                            else:
                                # Multiple colors reach same cell at same time
                                next_cells[(nr, nc)] = max(next_cells[(nr, nc)], color)
            
            # Color all cells at next level and add to queue
            for (r, c), color in next_cells.items():
                grid[r][c] = color
                queue.append((r, c, color))
        
        return grid