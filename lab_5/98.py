class Solution(object):
    def isValidBST(self, root):
        def validate(node, min_val, max_val):
            # Пустое дерево - валидное BST
            if not node:
                return True
            
            # Проверяем, что значение узла в допустимом диапазоне
            if not (min_val < node.val < max_val):
                return False
            
            # Рекурсивно проверяем левое и правое поддеревья
            # Для левого поддерева: все значения должны быть < node.val
            # Для правого поддерева: все значения должны быть > node.val
            return (validate(node.left, min_val, node.val) and 
                   validate(node.right, node.val, max_val))
        
        # Начинаем с бесконечных границ
        return validate(root, float('-inf'), float('inf'))