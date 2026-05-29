class Solution(object):
    def cloneGraph(self, node):
        # Обработка пустого графа
        if not node:
            return None
        
        # Словарь для сопоставления оригинальных узлов с их клонами
        cloned_nodes = {}
        
        # Создаем клон стартового узла
        cloned_nodes[node] = Node(node.val)
        
        # Используем очередь для BFS обхода
        from collections import deque
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            
            # Проходим по всем соседям текущего узла
            for neighbor in current.neighbors:
                # Если сосед еще не был клонирован
                if neighbor not in cloned_nodes:
                    # Клонируем соседа
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    # Добавляем в очередь для обработки его соседей
                    queue.append(neighbor)
                
                # Добавляем клонированного соседа в список соседей клонированного текущего узла
                cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])
        
        return cloned_nodes[node]