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
        while currentNode:
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

    def reverseWithStack(self):
        if self.isEmpty():
            print("List is empty")
            return
        oldHeadNode = self.head
        currentNode = self.head
        stack = []
        while currentNode:
            stack.append(currentNode)
            currentNode = currentNode.next
        oldHeadNode.next = None
        self.head = stack.pop()
        currentNode = self.head
        while len(stack) > 0:
            currentNode.next = stack.pop()
            currentNode = currentNode.next

    def reverseBest(self):
        currentNode = self.head
        prevNode = None
        while currentNode is not None:
            tempNext = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = tempNext
        self.head = prevNode

    def skip_arrange(self):
        currentNode = self.head
        connectionNode = currentNode.next
        runnerNode = connectionNode
        while(runnerNode != None):
            tempNext = currentNode.next
            runnerNode = runnerNode.next
            currentNode.next = runnerNode
            currentNode = tempNext
            if currentNode.next is None:
                currentNode.next = connectionNode

    @classmethod
    def addList(cls, list1, list2):
        stack1 = []
        stack2 = []
        cur_node1 = list1.head
        cur_node2 = list2.head
        new_list = Linkedlist()
        carry = 0
        while cur_node1:
            stack1.append(cur_node1.data)
            cur_node1 = cur_node1.next
        while cur_node2:
            stack2.append(cur_node2.data)
            cur_node2 = cur_node2.next
        length_tracker = greater_length_stack(stack1, stack2)
        while stack1 or stack2:
            if length_tracker == 1:
                sum = (custom_pop(stack1) + custom_pop(stack2) + carry)
                result = sum % 10
                new_list.addToFront(result)
                if sum > 9:
                    new_list.addToFront(sum // 10)
            else:
                sum = (custom_pop(stack1) + custom_pop(stack2) + carry)
                result = sum % 10
                carry = sum // 10
                new_list.addToFront(result)
                length_tracker -= 1
        return new_list

    @classmethod
    def addListReverse(cls, list1, list2):
        cur_node1 = list1.head
        cur_node2 = list2.head
        carry = 0
        new_list = Linkedlist()
        greatest_length = greatest_length_list(list1, list2)
        while cur_node1 or cur_node2:
            if greatest_length == 1:
                sum = (get_cur_value(cur_node1) +
                       get_cur_value(cur_node2)) + carry
                result = sum % 10
                new_list.addToFront(result)
                if sum > 9:
                    new_list.addToFront(sum // 10)
            else:
                sum = (get_cur_value(cur_node1) +
                       get_cur_value(cur_node2)) + carry
                result = sum % 10
                carry = sum // 10
                new_list.addToFront(result)
                greatest_length -= 1
            if cur_node1:
                cur_node1 = cur_node1.next
            if cur_node2:
                cur_node2 = cur_node2.next
        return new_list

    @classmethod
    def merge_list(cls, list1, list2):
        #  length = greatest_length_list(list1, list2)
        cur_node1 = list1.head
        cur_node2 = list2.head
        new_list = Linkedlist()
        while cur_node1 and cur_node2:
            if cur_node1.data <= cur_node2.data:
                new_list.addNode(cur_node1.data)
                cur_node1 = cur_node1.next
            else:
                new_list.addNode(cur_node2.data)
                cur_node2 = cur_node2.next
        while cur_node1:
            new_list.addNode(cur_node1.data)
            cur_node1 = cur_node1.next
        while cur_node2:
            new_list.addNode(cur_node2.data)
            cur_node2 = cur_node2.next
        return new_list

    @classmethod
    def merge_arr_list(cls, linkedlist_arr):
        merge = cls.merge_list(linkedlist_arr[0], linkedlist_arr[1])
        for i in range(2, len(linkedlist_arr)):
            merge = cls.merge_list(merge, linkedlist_arr[i])
        return merge


def greatest_length_list(list1, list2):
    length1 = list1.getLength()
    length2 = list2.getLength()
    if length1 >= length2:
        return length1
    else:
        return length2


def get_cur_value(node):
    if node is None:
        return 0
    return node.data


def custom_pop(stack):
    if len(stack) != 0:
        return stack.pop()
    return 0


def greater_length_stack(stack1, stack2):
    if len(stack1) >= len(stack2):
        return len(stack1)
    else:
        return len(stack2)


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
myArr = [2, 3]
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
# secondList.reverse()
# secondList.printList()
# secondList.reverseWithStack()
# secondList.printList()
secondList.printList()
secondList.reverseBest()
secondList.printList()
new_dict = {}
new_dict['a'] = 0
print(new_dict['a'])
if('a' in new_dict):
    print('okay')

newList = Linkedlist()
newList.addNode(1)
newList.addNode(2)
newList.addNode(3)
newList.addNode(4)
newList.addNode(5)
newList.addNode(6)
newList.addNode(7)
newList.addNode(8)
newList.addNode(9)
print('\n')
newList.printList()
newList.skip_arrange()
print('\n')
newList.printList()

first_sum = Linkedlist()
first_sum.addNode(9)
first_sum.addNode(9)
# first_sum.addNode(3)
# first_sum.addNode(4)


second_sum = Linkedlist()
second_sum.addNode(5)
second_sum.addNode(5)
# second_sum.addNode(7)
f1 = Linkedlist()
f2 = Linkedlist()
f1.addNode(1)
f1.addNode(2)
f1.addNode(3)
f2.addNode(4)
f2.addNode(5)
f2.addNode(8)
f2.addNode(9)
resulant_sum = Linkedlist.addList(first_sum, second_sum)
resulant_sum2 = Linkedlist.addListReverse(f1, f2)
print('\n')
# resulant_sum.printList()
print('\n')
resulant_sum2.printList()
merge1 = Linkedlist()
merge1.addNode(1)
merge1.addNode(3)
merge1.addNode(5)

merge2 = Linkedlist()
merge2.addNode(2)
merge2.addNode(4)
merge2.addNode(6)
print('\n')
merge3 = Linkedlist()
merge3.addNode(0)
merge3.addNode(10)
merge3.addNode(100)
#merged = Linkedlist.merge_list(merge1, merge2)
merged = Linkedlist.merge_arr_list([merge1, merge2, merge3])
merged.printList()

for i in range(2, 3):
    print('wooo')
