class Solution(object):
    def levelOrder(self, root):
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # Если мы на новом уровне, создаём новый список
            if len(result) == level:
                result.append([])
            
            # Добавляем узел на его уровень
            result[level].append(node.val)
            
            # Рекурсивно обходим детей со следующим уровнем
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result