from inputTree import node1

def postOrder(root):
    if root is None:
        return 

    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

postOrder(node1)