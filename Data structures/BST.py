class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.key, end=' ')
            self._inorder(root.right)

# Example usage
bst = BST()
for value in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(value)

print("Inorder traversal:")
bst.inorder()

key_to_search = 40
found = bst.search(key_to_search)
if found:
    print(f"Key {key_to_search} found in BST.")
else:
    print(f"Key {key_to_search} not found in BST.")
