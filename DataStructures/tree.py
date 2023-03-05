"""GeekforGeeks"""
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def preOrderTree(root):
    if root:
        print(root.val)
        preOrderTree(root.left)
        preOrderTree(root.right)


def inOrderTree(root):
    if root:
        inOrderTree(root.left)
        print(root.val)
        inOrderTree(root.right)


def postOrderTree(root):
    if root:
        postOrderTree(root.left)
        postOrderTree(root.right)
        print(root.val)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("preorder traversal of binary tree is")
    preOrderTree(root)

    print("Inorder traversal of binary tree is")
    inOrderTree(root)

    print("postorder traversal of binary tree is")
    postOrderTree(root)