from inputTree import node1

def height(root):
    if root is None:
        return 0      # if we consider height as no of levels then return 0
                    # if we consider height as ground to root then return -1
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return 1 + max(leftHeight , rightHeight)

print(height(node1))