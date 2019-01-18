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
        tempNode = self.head
        while tempNode is not None:
            index = index + 1
            tempNode = tempNode.next
        return index

    def getLength(self):
        length = 0
        tempNode = self.head
        while tempNode is not None:
            length = length + 1
            tempNode = tempNode.next
        return length

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

    def addNodeAfterValue(self, data, searchValue):
        if self.isEmpty():
            print("List is empty")
            return
        newNode = Node(data)
        tempNode = self.head
        nextNode = None
        while tempNode is not None:
            if tempNode.data == searchValue:
                if(tempNode.next):
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                    return
                tempNode.next = newNode
                return
            tempNode = tempNode.next
        print(f'could not find value: {searchValue}')

    def addNodeBeforeValue(self, data, searchValue):
        if self.isEmpty():
            print("List is empty")
            return
        tempNode = self.head
        newNode = Node(data)
        prevNode = None
        while tempNode is not None:
            if tempNode.data == searchValue:
                if(tempNode == self.head):
                    self.head = newNode
                    newNode.next = tempNode
                    return
                prevNode.next = newNode
                newNode.next = tempNode
                return
            prevNode = tempNode
            tempNode = tempNode.next
        print(f'could not find value: {searchValue}')

    def addNodeAtIndex(self, data, searchIndex):
        if self.isEmpty():
            print('List is empty')
            return
        tempNode = self.head
        newNode = Node(data)
        index = 0
        prevNode = None
        while index <= searchIndex:
            if tempNode is None:
                print(f'Index is out of bounds for: {searchIndex}')
                return
            if searchIndex == 0:
                self.head = newNode
                newNode.next = tempNode
                return
            if(tempNode.next is None and index == searchIndex):
                tempNode.next = newNode
                return
            if index == searchIndex:
                prevNode.next = newNode
                newNode.next = tempNode
                return

            index = index + 1
            prevNode = tempNode
            tempNode = tempNode.next

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

    def getAvgValue(self):
        if self.isEmpty():
            return 0
        tempNode = self.head
        total = 0
        while tempNode is not None:
            total = total + tempNode.data
            tempNode = tempNode.next
        return total / self.getLength()


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
