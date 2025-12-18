class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.height = 1

def altura(n):
    return n.height if n else 0

def rot_dir(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(altura(y.left), altura(y.right))
    x.height = 1 + max(altura(x.left), altura(x.right))
    return x

def inserir(node, k):
    if not node:
        return Node(k)
    if k < node.key:
        node.left = inserir(node.left, k)
    else:
        node.right = inserir(node.right, k)

    node.height = 1 + max(altura(node.left), altura(node.right))
    return node
