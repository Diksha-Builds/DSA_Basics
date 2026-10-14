class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    head = None
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        print()
        print("List elements : ")
        temp = self.head
        while(True):
            print(temp.data, end=" ")
            temp = temp.next
            if(temp == self.head):
                break

lobj = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

lobj.append(n1)
lobj.append(n2)
lobj.append(n3)
lobj.append(n4)
lobj.append(n5)

lobj.display()