
class Node(object):
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.top = None

    def recursBST(self, node, data):
        if node is None:
            node = Node(data)
        elif self.top.root > data:
            node.left = self.recursBST(node.left, data)
        elif  self.top.root < data:
            node.right = self.recursBST(node.right, data)

        return node

    def insert(self, data):
        self.top = self.recursBST(self.top, data)

conv = BST()
print(conv.insert(8))
print(conv.insert(3))
print(conv.insert(6))
print(conv.insert(1))
print(conv.insert(-1))
print(conv.insert(10))
print(conv.insert(14))
print(conv.insert(50))

