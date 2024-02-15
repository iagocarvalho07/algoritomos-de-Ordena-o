class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def print_preorder(self):
        self._print_preorder(self.root)

    def _print_preorder(self, current_node):
        if current_node is not None:
            print(current_node.value)
            self._print_preorder(current_node.left)
            self._print_preorder(current_node.right)

    def print_inorder(self):
        self._print_inorder(self.root)

    def _print_inorder(self, current_node):
        if current_node is not None:
            self._print_inorder(current_node.left)
            print(current_node.value)
            self._print_inorder(current_node.right)

    def print_postorder(self):
        self._print_postorder(self.root)

    def _print_postorder(self, current_node):
        if current_node is not None:
            self._print_postorder(current_node.left)
            self._print_postorder(current_node.right)
            print(current_node.value)



