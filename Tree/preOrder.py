# class Node:
#     def __init__(self, data):
#         self.data =data
#         self.left = None
#         self.right = None

from node import Node

def preOrder(root):
    if root is None:
        return None

    print(root.data)
    preOrder(root.left)
    preOrder(root.right)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
node6.left = node10
node6.right = node11


preOrder(node1)
