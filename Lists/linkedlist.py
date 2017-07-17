class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        current = self.head
        new_node = Node(data)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            while current.next is not None:
                current = current.next
            # add to front
            new_node.next = self.head
            self.head = new_node

            # add to back
            # new_node.next = None
            # self.tail.next = new_node
            # self.tail = new_node


    def remove(self, data):
        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next

    def removeDupes(self):
        lst = []

        current = self.head

        while current.next is not None:
            if current.next.data not in lst:
                current = current.next
                lst.append(current.data)
            else:
                current.next = current.next.next

    def _print(self):
        current = self.head

        while current is not None:
            print current.data,
            current = current.next

    
ll = LinkedList()
ll.add(3)
ll.add(5)
ll.add(8)
ll.add(5)
ll.add(10)
ll.add(2)
ll.add(1)


