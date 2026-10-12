''' Find the middle node and delete it '''

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

    def deleteMiddle(self):
        if(self.head == None):
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head
        prev = None

        while(fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        print("Middle element is : ",slow.data)
        prev.next = slow.next
        slow = None
    
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

print("Insertion of nodes : ")
lobj.append(nobj1)
lobj.append(nobj2)
lobj.append(nobj3)
lobj.append(nobj4)
lobj.append(nobj5)
lobj.append(nobj6)

lobj.print()

lobj.deleteMiddle()
lobj.print()