from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def isLeaf(self, node):
        return node.right is None and node.left is None

    def getRootValue(self):
        return self.root.data

    def addNode(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.root = newNode
            return
        currentNode = self.root
        while True:
            if newNode.data < currentNode.data:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return
                currentNode = currentNode.left
            if newNode.data > currentNode.data:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return
                currentNode = currentNode.right

    def getHeight(self, root):
        if root is None:
            return 0
        leftTree = self.getHeight(root.left)
        rightTree = self.getHeight(root.right)
        return max(leftTree, rightTree) + 1

    def preOrder(self, root):
        if root is None:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)

    def bredthFirst(self):
        if self.isEmpty():
            print("Tree is empty")
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            currentNode = queue.pop()
            print(currentNode.data)
            if currentNode.left is not None:
                queue.appendleft(currentNode.left)
            if currentNode.right is not None:
                queue.appendleft(currentNode.right)

    def isValue(self, data):
        if self.isEmpty():
            print("Tree is empty")
            return False
        currentNode = self.root
        while currentNode:
            if data > currentNode.data:
                currentNode = currentNode.right
            elif data < currentNode.data:
                currentNode = currentNode.left
            else:
                return True
        return False

    def searchByValue(self, data):
        if self.isEmpty():
            print("Tree is empty")
            return False
        currentNode = self.root
        while currentNode:
            if data > currentNode.data:
                currentNode = currentNode.right
            elif data < currentNode.data:
                currentNode = currentNode.left
            else:
                return currentNode.data
        return False

    def get_level(self, root, data):
        if data == root.data:
            return 1
        if self.root.left:
            return self.get_level(self.root.left, data) + 1
        elif self.root.right:
            return self.get_level(self.root.right, data) + 1
        return 0


my_tree = BinaryTree()
# print(my_tree.isEmpty())
my_tree.addNode(50)
my_tree.addNode(75)
my_tree.addNode(60)
my_tree.addNode(40)
my_tree.addNode(45)
# print(my_tree.root.data)
# print(my_tree.root.left.right.data)
print(my_tree.getHeight(my_tree.root))
# my_tree.postOrder(my_tree.root)
my_tree.bredthFirst()
print(my_tree.get_level(my_tree.root, 75))
