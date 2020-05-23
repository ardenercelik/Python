class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        counter = 0
        currentNode = self.head
        while currentNode != None:
            counter = counter + 1
            currentNode = currentNode.next
        return counter
        
    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        currentNode = self.head
        if data == None:
            return None
        node = Node(data)
        if currentNode == None:
            self.head = node
            return node
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node
        return node
        

    def find(self, data):
        currentNode = self.head
        if data == None:
            return None
        if currentNode == None:
            return None
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                return currentNode
            currentNode = currentNode.next
        return None
        

    def delete(self, data):
        if data == None:
            return
        if self.head == None:
            return
        currentNode = self.head.next
        prevNode = self.head
        if currentNode == None:
            prevNode.next = None
            return 
        while currentNode.next is not None:
            if currentNode.data == data:
                prevNode.next = currentNode.next
                return 
            prevNode = currentNode
            currentNode = currentNode.next
        return None


    def print_list(self):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next == None:
                print("{}".format(currentNode.data), end="")
            else:
                print("{} => ".format(currentNode.data), end="")
            currentNode = currentNode.next


    def get_all_data(self):
        res = []
        currentNode = self.head
        while currentNode is not None:
            res.append(currentNode.data)
            currentNode = currentNode.next
        return res


a = LinkedList()
a.insert_to_front(10)
print(len(a))
print(a.get_all_data())
a.insert_to_front("a")
a.insert_to_front("bc")
print(a.get_all_data())
a.insert_to_front(None)
print(a.get_all_data())
print(len(a))


b = LinkedList()
b.append(10)
print(len(b))
print(b.get_all_data())
b.append("a")
b.append("bc")
print(b.get_all_data())
b.append(None)
print(b.get_all_data())
print(len(b))

b.print_list()


