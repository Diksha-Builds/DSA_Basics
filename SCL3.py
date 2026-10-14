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

    def insert(self, new_node, pos):
        if pos == 1:    # inserting at first position
            temp = self.head
            while(temp.next != self.head):  # find last node
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        else: # inserting node from 2nd to last position
            p = 1
            temp = self.head
            while(p != pos-1):
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next =  new_node

    def delete(self, value):
        temp = self.head
        prev = None

        # deleting first node
        if temp.data == value:
            while(temp.next != self.head):  # find last node
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            while(temp.data != value and temp != None):
                prev = temp
                temp = temp.next
                if(temp == self.head):
                    print("Value is not present in the list")
                    return
            prev.next = temp.next
            temp = None

    def display(self):
        temp = self.head
        while(True):
            print(temp.data, end=" ")
            temp = temp.next
            if(temp == self.head):
                break
        print("\n")

lobj = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

print("Appending nodes : \n")
lobj.append(n1)
lobj.append(n2)
lobj.append(n3)
lobj.append(n4)
lobj.append(n5)

lobj.display()

n6 = Node(35)

print("Insertion of a node at a specific position : \n")
lobj.insert(n6, 4)
lobj.display()

print("Deletion of a node :\n")
lobj.delete(35)
lobj.display()