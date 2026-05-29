class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r, c):
            # Стек для DFS
            stack = [(r, c)]
            visited.add((r, c))
            
            while stack:
                row, col = stack.pop()
                # Проверяем всех соседей (вверх, вниз, влево, вправо)
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    # Проверяем границы и является ли клетка землей
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == '1' and 
                        (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        stack.append((new_row, new_col))
        
        # Проходим по всем клеткам
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        
        return islands