from Node import Node  # Importing the Node class from Node.py

class RedBlackTree():
    def __init__(self):
        self.TNULL= Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL



    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, node):
     while node != self.root and node.parent.color == 1:
        if node.parent.parent is None:
            break
        grandparent = node.parent.parent

        if node.parent == grandparent.right:
            uncle = grandparent.left
            if uncle and uncle.color == 1:
            #case 1:uncle is red
                uncle.color = 0
                node.parent.color = 0
                grandparent.color = 1
                node = grandparent  # Needed for the next loop
            else:
                if node == node.parent.left:
                    #case 2: node is left child
                    node = node.parent  
                    self.right_rotate(node)
                #case 3:node is right child
                node.parent.color = 0
                grandparent.color = 1
                self.left_rotate(grandparent)
        else:
            uncle = grandparent.right
            if uncle and uncle.color == 1:
                # mirror case 1
                uncle.color = 0
                node.parent.color = 0
                grandparent.color = 1
                node = grandparent
            else:
                if node == node.parent.right:
                    # mirror case 2
                    node = node.parent
                    self.left_rotate(node)
                # mirror case 3
                node.parent.color = 0
                grandparent.color = 1
                self.right_rotate(grandparent)

     self.root.color = 0

def left_rotate(self, x):
     y = x.right
     x.right = y.left
     if y.left != self.TNULL:
        y.left.parent = x
     y.parent = x.parent
     if x.parent is None:
        self.root = y
     elif x == x.parent.left:
        x.parent.left = y
     else:
        x.parent.right = y
     y.left = x
     x.parent = y

def right_rotate(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.TNULL:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:
        self.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y


