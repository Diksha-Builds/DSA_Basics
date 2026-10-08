# Reversing the Linked List

class Node :

    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_node):
            print("After appending a new node : ")

            if(self.head == None):
                self.head = new_node
            else:
                temp = self.head
    
                while(temp.next):   # temp.next != None
                    temp = temp.next
    
                temp.next = new_node    # appending new node

    def insert(self, new_node, pos):
        print("After inserting a new node : ")

        if pos == 1:    # inserting at first position
            new_node.next = self.head
            self.head = new_node
        else: # inserting node from 2nd to last position
            p = 1
            temp = self.head
            while(p != pos-1 and temp.next != None):
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next =  new_node

    def del_node(self, value):
        temp = self.head
        prev = None

        print("After deleting a node : ")

        # deleting first node
        if temp.data == value:
            self.head = self.head.next
            return
        while(temp):
            if temp.data == value:  # searching value
                break
            else:                   # traverse
                prev = temp
                temp = temp.next

        if temp == None:            # value is not present
            print("Value is not present in the list")
            return
        prev.next = temp.next
        temp = None

    def reverse(self):
        curr = self.head
        prev = None

        print("After reversing the linked list : ")

        while(curr):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        self.head = prev

    def print(self):
        temp = self.head

        while temp:     # temp != None
            print(temp.data)
            temp = temp.next

list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))
list.print()

list.insert(Node(100), 1)
list.print()
list.insert(Node(66), 7)
list.print()

list.del_node(40)
list.print()

list.reverse()
list.print()