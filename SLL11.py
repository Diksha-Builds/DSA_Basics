''' Concatenate 2 linked lists '''

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

    def concatenate(self, head2):

        temp = self.head

        while(temp.next != None):
            temp = temp.next

        temp.next = head2   # head of lobj2
    
    def print(self):
        temp = self.head

        while(temp != None):
            print(temp.data)
            temp = temp.next

lobj1 = LinkedList()

nobj1 = Node(10)
nobj2 = Node(20)
nobj3 = Node(30)
nobj4 = Node(40)
nobj5 = Node(50)
nobj6 = Node(60)

print("Linked List 1 : ")
lobj1.append(nobj1)
lobj1.append(nobj2)
lobj1.append(nobj3)
lobj1.append(nobj4)
lobj1.append(nobj5)
lobj1.append(nobj6)

lobj1.print()

lobj2 = LinkedList()

nobj1 = Node(15)
nobj2 = Node(25)
nobj3 = Node(35)
nobj4 = Node(45)
nobj5 = Node(55)
nobj6 = Node(65)

print("Linked List 2 : ")
lobj2.append(nobj1)
lobj2.append(nobj2)
lobj2.append(nobj3)
lobj2.append(nobj4)
lobj2.append(nobj5)
lobj2.append(nobj6)

lobj2.print()

print("After concatenation : ")
lobj1.concatenate(lobj2.head)

lobj1.print()