"""
https://www.educative.io/answers/how-to-solve-a-binary-tree-preorder-traversal-iteratively
https://www.educative.io/answers/how-to-do-a-post-order-traversal-of-a-binary-tree-using-stacks
https://www.educative.io/answers/how-to-perform-an-iterative-inorder-traversal-of-a-binary-tree
"""
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

def preOrderTreeStack(root):
    preorder = []
    stack1 = [root]

    while stack1:
        node = stack1.pop()
        if node:
            preorder.append(node.val)
            stack1.append(node.right)
            stack1.append(node.left)
    return preorder


def inOrderTree(root):
    if root:
        inOrderTree(root.left)
        print(root.val)
        inOrderTree(root.right)

def inOrderTreeStack(root):
    preorder = []
    stack1 = [root]

    while stack1:
        node = stack1.pop()
        if node:
            stack1.append(node.right)
            preorder.append(node.val)
            stack1.append(node.left)
    return preorder

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

    print("preorder traversal of binary tree using stack is")
    print(preOrderTreeStack(root))

    print("Inorder traversal of binary tree is")
    inOrderTree(root)

    print("preorder traversal of binary tree using stack is")
    print(inOrderTreeStack(root))

    print("postorder traversal of binary tree is")
    postOrderTree(root)