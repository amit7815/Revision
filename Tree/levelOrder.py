import queue
from inputTree import node1

def levelOrder(root):
    if root is None:
        return

    q = queue.Queue()

    q.put(root)
    while q.empty() is False:
        current_element = q.get()
        print(current_element.data)
        if current_element.left is not None:
            q.put(current_element.left)
        if current_element.right is not None:
            q.put(current_element.right)

levelOrder(node1)