class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Множества для хранения клеток, которые могут достичь каждого океана
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            # Проверяем границы и был ли уже посещен
            if (r < 0 or r >= m or c < 0 or c >= n or 
                (r, c) in visited or 
                heights[r][c] < prev_height):
                return
            
            # Добавляем текущую клетку в посещенные
            visited.add((r, c))
            
            # Идем в 4 направлениях
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        # Запускаем DFS от границ, прилегающих к Тихому океану (верхняя и левая границы)
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])  # левый край
            dfs(i, n - 1, atlantic, heights[i][n - 1])  # правый край
        
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])  # верхний край
            dfs(m - 1, j, atlantic, heights[m - 1][j])  # нижний край
        
        # Находим пересечение - клетки, которые могут достичь обоих океанов
        result = [list(cell) for cell in pacific & atlantic]
        
        return result