from inputTree import node1

def nodeWithLargestData(root):
    if root is None:
        return -1000000

    leftLargest = nodeWithLargestData(root.left)
    rightLargest = nodeWithLargestData(root.right)

    return max(leftLargest, rightLargest, root.data)

def nodeWithMinimumData(root):
    if root is None:
        return 100000000

    leftMinimum = nodeWithMinimumData(root.left)
    rightMinimum = nodeWithMinimumData(root.right)

    return min(leftMinimum, rightMinimum, root.data)
print(f'maximum data is  {nodeWithLargestData(node1)}')
print(f'minimum data is  {nodeWithMinimumData(node1)}')
