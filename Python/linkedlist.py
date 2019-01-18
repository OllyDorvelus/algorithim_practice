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

    def getTotalIndex(self):
        index = -1
        currentNode = self.head
        while currentNode is not None:
            index = index + 1
            currentNode = currentNode.next
        return index

    def getLength(self):
        length = 0
        currentNode = self.head
        while currentNode is not None:
            length = length + 1
            currentNode = currentNode.next
        return length

    def printList(self):
        if self.isEmpty():
            print("List is empty")
            return
        currentNode = self.head
        while(currentNode is not None):
            print(currentNode.data)
            currentNode = currentNode.next

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
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = Node(data)

    def removeHead(self):
        if self.isEmpty():
            print("can't remove from empty list")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next

    def addNodeAfterValue(self, data, searchValue):
        if self.isEmpty():
            print("List is empty")
            return
        newNode = Node(data)
        currentNode = self.head
        nextNode = None
        while currentNode is not None:
            if currentNode.data == searchValue:
                if(currentNode.next):
                    nextNode = currentNode.next
                    currentNode.next = newNode
                    newNode.next = nextNode
                    return
                currentNode.next = newNode
                return
            currentNode = currentNode.next
        print(f'could not find value: {searchValue}')

    def addNodeBeforeValue(self, data, searchValue):
        if self.isEmpty():
            print("List is empty")
            return
        currentNode = self.head
        newNode = Node(data)
        prevNode = None
        while currentNode is not None:
            if currentNode.data == searchValue:
                if(currentNode == self.head):
                    self.head = newNode
                    newNode.next = currentNode
                    return
                prevNode.next = newNode
                newNode.next = currentNode
                return
            prevNode = currentNode
            currentNode = currentNode.next
        print(f'could not find value: {searchValue}')

    def addNodeAtIndex(self, data, searchIndex):
        if self.isEmpty():
            print('List is empty')
            return
        currentNode = self.head
        newNode = Node(data)
        index = 0
        prevNode = None
        while index <= searchIndex:
            if currentNode is None:
                print(f'Index is out of bounds for: {searchIndex}')
                return
            if searchIndex == 0:
                self.head = newNode
                newNode.next = currentNode
                return
            if(currentNode.next is None and index == searchIndex):
                currentNode.next = newNode
                return
            if index == searchIndex:
                prevNode.next = newNode
                newNode.next = currentNode
                return

            index = index + 1
            prevNode = currentNode
            currentNode = currentNode.next

    def getMaxValue(self):
        if self.isEmpty():
            return None
        currentNode = self.head
        maxValue = currentNode.data
        while currentNode.next is not None:
            if currentNode.data > maxValue:
                maxValue = currentNode.data
            currentNode = currentNode.next
        return maxValue

    def getMinValue(self):
        if self.isEmpty():
            return None
        currentNode = self.head
        minValue = currentNode.data
        while currentNode.next is not None:
            if currentNode.data < minValue:
                minValue = currentNode.data
            currentNode = currentNode.next
        return minValue

    def getAvgValue(self):
        if self.isEmpty():
            return 0
        currentNode = self.head
        total = 0
        while currentNode is not None:
            total = total + currentNode.data
            currentNode = currentNode.next
        return total / self.getLength()

    def reverse(self):
        if self.isEmpty():
            print("List is empty")
            return
        currentNode = self.head
        nextNode = None
        prevNode = None
        while currentNode.next is not None:
            currentNode = currentNode.next
        while currentNode != self.head:
            nextNode = self.head.next
            currentNode.next = self.head
            self.head.next = prevNode
            prevNode = self.head
            self.head = nextNode


myList = Linkedlist()
secondList = Linkedlist()
# myList.addNode(3)
# myList.addNode(4)
# myList.addNode(5)
myList.addNode(10)
myList.addNode(20)
myList.addNode(30)
myList.addNode(40)
myList.addNode(50)

# myList.addNodeBeforeValue(100, 10)
# myList.addNodeAtIndex(200, 2)
# myList.addNodeAtIndex(500, 6)


# myList.removeHead()
# myList.removeHead()
# myList.removeHead()
myList.printList()
print('max is ', myList.getMaxValue())
print('min is ', myList.getMinValue())
print('avg is ', myList.getAvgValue())
print('head is', myList.getHeadValue())
print('Total indexs', myList.getTotalIndex())
print('head is', myList.getHeadValue())

secondList.addNode('A')
secondList.addNode('B')
secondList.addNode('C')
secondList.addNode('D')
secondList.reverse()
secondList.printList()
