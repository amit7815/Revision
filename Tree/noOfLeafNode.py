from inputTree import node1

def countLeafNode(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1 

    leftcount = countLeafNode(root.left)
    rightcount = countLeafNode(root.right)

    return leftcount + rightcount

print(countLeafNode(node1))