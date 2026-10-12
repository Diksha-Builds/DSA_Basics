''' Write a function to delete alternate node in SLL '''

class Node:

    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_node):

        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head

            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

    def delAlternate(self):
        prev = self.head
        temp = self.head.next
    
        while(prev != None and temp != None):
            prev.next = temp.next
            temp = None     # delete the node
            prev = prev.next

            if(prev):
                temp = prev.next
    
    def print(self):
        temp = self.head

        while(temp != None):
            print(temp.data)
            temp = temp.next

lobj = LinkedList()

nobj1 = Node(10)
nobj2 = Node(20)
nobj3 = Node(30)
nobj4 = Node(40)
nobj5 = Node(50)
nobj6 = Node(60)

print("Insertion of a node at the end of the Linked List : ")
lobj.append(nobj1)
lobj.append(nobj2)
lobj.append(nobj3)
lobj.append(nobj4)
lobj.append(nobj5)
lobj.append(nobj6)

lobj.print()

print("Deletion of alternate nodes : ")
lobj.delAlternate()

lobj.print()