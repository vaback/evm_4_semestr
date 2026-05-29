class Solution(object):
    def invertTree(self, root):
        # Базовый случай: если узел пустой, возвращаем None
        if not root:
            return None
        
        # Меняем местами левое и правое поддеревья
        root.left, root.right = root.right, root.left
        
        # Рекурсивно инвертируем левое и правое поддеревья
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root