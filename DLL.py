class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:
    head = None
    

    def append(self, new_node):
        temp = self.head
        
        if temp != None:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:   # First Node
            self.head = new_node

    def print(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

lobj = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

print("After appending : ")
lobj.append(n1)
lobj.append(n2)
lobj.append(n3)
lobj.append(n4)

lobj.print()