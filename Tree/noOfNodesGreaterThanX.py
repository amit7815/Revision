from inputTree import node1

def noOfNodeGreaterThanX(root, x):
    if root is None:
        return 0

    leftCount = noOfNodeGreaterThanX(root.left, x)
    rightCount = noOfNodeGreaterThanX(root.right, x)

    if root.data > x:
        return 1 + leftCount + rightCount

    else:
        return leftCount + rightCount


x = int(input())
print(noOfNodeGreaterThanX(node1, x))