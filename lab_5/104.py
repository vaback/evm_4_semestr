class Solution(object):
    def maxDepth(self, root):
        # Базовый случай: если узел пустой, глубина = 0
        if not root:
            return 0
        
        # Рекурсивно находим максимальную глубину левого и правого поддеревьев
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Возвращаем максимальную глубину + 1 (текущий узел)
        return max(left_depth, right_depth) + 1