class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        def _walk(root):
            if root is None:
                return []

            result = [root.value]
            result += _walk(root.left)
            result += _walk(root.right)
            return result

        return _walk(self.root)

    def in_order(self):
        def _walk(root):
            if root is None:
                return []

            result = _walk(root.left)
            result.append(root.value)
            result += _walk(root.right)
            return result

        return _walk(self.root)

    def post_order(self):
        def _walk(root):
            if root is None:
                return []

            result = _walk(root.left)
            result += _walk(root.right)
            result.append(root.value)
            return result

        return _walk(self.root)
    
    def find_maximum_value(self):
        def _find_maximum(root):
            if root is None:
                return float('-inf')

            max_left = _find_maximum(root.left)
            max_right = _find_maximum(root.right)

            return max(max_left, max_right, root.value)

        return _find_maximum(self.root)


class BinarySearchTree(BinaryTree):
    def add(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)

            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)

            return root

        self.root = _insert(self.root, value)

    def contains(self, value):
        def _search(root, value):
            if not root:
                return False

            if root.value == value:
                return True

            if value < root.value:
                return _search(root.left, value)
            else:
                return _search(root.right, value)

        return _search(self.root, value)
    
    
if __name__=="__main__":
        bst = BinarySearchTree()
        bst.add(8)
        bst.add(3)
        bst.add(10)
        bst.add(1)
        bst.add(6)
        bst.add(14)
        bst.add(4)
        bst.add(7)
        bst.add(13)

        print(bst.contains(6))  # True
        print(bst.contains(12))  # False

        bst.pre_order()  # Pre-order traversal
        # Output: 8 3 1 6 4 7 10 14 13

        bst.in_order()  # In-order traversal
        # Output: 1 3 4 6 7 8 10 13 14

        bst.post_order()  # Post-order traversal
        # Output: 1 4 7 6 3 13 14 10 8
        
        maximum_value = bst.find_maximum_value()
        print('max = ',maximum_value)