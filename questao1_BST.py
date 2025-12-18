class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, k, v):
        self.root = self._put(self.root, k, v)

    def _put(self, node, k, v):
        if node is None:
            return Node(k, v)
        if k < node.key:
            node.left = self._put(node.left, k, v)
        elif k > node.key:
            node.right = self._put(node.right, k, v)
        else:
            node.value = v
        return node
