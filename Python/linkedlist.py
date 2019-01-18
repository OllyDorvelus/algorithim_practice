class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return not self.head

    def getHeadValue(self):
        if self.isEmpty():
            return None
        return self.head.data

    def printList(self):
        if self.isEmpty():
            print("List is empty")
            return
        tempNode = self.head
        while(tempNode is not None):
            print(tempNode.data)
            tempNode = tempNode.next

    def addToFront(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def addNode(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        tempNode = self.head
        while tempNode.next is not None:
            tempNode = tempNode.next
        tempNode.next = Node(data)

    def removeHead(self):
        if self.isEmpty():
            print("can't remove from empty list")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next

    def addNodeAfterValue(self, value):
        pass

    def addNodeBeforeValue(self, value):
        pass

    def addNodeBeforeIndex(self, index):
        pass

    def addNodeAfterIndex(self, index):
        pass

    def getMaxValue(self):
        if self.isEmpty():
            return None
        tempNode = self.head
        maxValue = tempNode.data
        while tempNode.next is not None:
            if tempNode.data > maxValue:
                maxValue = tempNode.data
            tempNode = tempNode.next
        return maxValue

    def getMinValue(self):
        if self.isEmpty():
            return None
        tempNode = self.head
        minValue = tempNode.data
        while tempNode.next is not None:
            if tempNode.data < minValue:
                minValue = tempNode.data
            tempNode = tempNode.next
        return minValue


myList = Linkedlist()
# myList.addNode(3)
# myList.addNode(4)
# myList.addNode(5)
myList.addNode(10)
myList.addNode(20)
myList.addNode(30)
myList.removeHead()
myList.removeHead()
myList.removeHead()
myList.printList()
print('head is', myList.getHeadValue())


def sum():
    return 3
