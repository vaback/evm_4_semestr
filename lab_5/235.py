class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Используем свойство BST: левое поддерево < узел < правое поддерево
        while root:
            # Если оба узла меньше корня, ищем в левом поддереве
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Если оба узла больше корня, ищем в правом поддереве
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # Если узлы по разные стороны от корня или один из них равен корню
            else:
                return root