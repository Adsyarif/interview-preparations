class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def tree_height(root):
    # Base case: an empty tree has height 0
    if root is None:
        return 0
    else:
        return 1 + max(tree_height(root.left), tree_height(root.right))
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = tree_height(root)
print("Height of the binary tree:", result)

