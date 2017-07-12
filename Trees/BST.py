class Node:
    def __init__(self, val):
        self.val = val
        self.rightChild = None
        self.leftChild = None

    def getVal(self):
        return self.val

    def setVal(self, data):
        self.val = data

    def getChildren(self):
        children = []

        if self.leftChild is not None:
            children.append(self.leftChild.val)
        if self.rightChild is not None:
            children.append(self.rightChild.val)

        return children

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def setRoot(self, val):
        self.root = Node(val)

    def getRoot(self):
        return self.root

    def insert(self, val):
        # always start with self.root
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif val > currentNode.val :
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        # always start with self.root
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        # return false if we reach end of BST and value not found
        if currentNode is None:
            return False
        elif val == currentNode.val:
            return True
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def delete(self, val):
        if self.root is None:
            return None
        else:
            self.deleteNode(self.root, val)

    # not working, need to figure this out....
    def deleteNode(self, currentNode, val):
        # return false if we reach end of BST and value not found
        if currentNode is None:
            return False
        elif val == currentNode.val:
            currentNode.leftChild = None
            currentNode.rightChild = None
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def _print(self):
        # start with self.root
        current_level = [self.root]
        while current_level:
            next_level = list()
            # loop through each node in current_level and append to a new lst
            for node in current_level:
                # loop through each node in current_level and print out item
                print 'node: ', node.getVal()
                print 'children: ', node.getChildren()
                # checking if leftChild or rightChild exists
                if node.leftChild:
                    next_level.append(node.leftChild)
                if node.rightChild:
                    next_level.append(node.rightChild)
                # update current_level by setting it to next_level
                current_level = next_level

    def valid(self):
        # an empty tree is valid
        if self.root is None:
            return True

        return self.is_valid(self.root, float('-inf'), float('inf'))

    # returning False?
    def is_valid(self, currentNode, _min, _max):
        if currentNode.val <= _min:
            return False

        if currentNode.val >= _max:
            return False

        left_ok = True
        right_ok = True

        if currentNode.leftChild is not None:
            left_ok = self.is_valid(currentNode.leftChild, _min, currentNode.val)
        if currentNode.rightChild is not None:
            right_ok = self.is_valid(currentNode.rightChild, currentNode.val, _max)

        return left_ok and right_ok

        

    


tree = BST()
tree.setRoot(1)
tree.insert(2)
tree.insert(25)
tree.insert(7)
tree.insert(5)
tree.insert(10)
tree.insert(7)
tree.insert(2)