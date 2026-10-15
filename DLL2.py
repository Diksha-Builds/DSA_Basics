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

    def insert(self, new_node, pos):
        temp = self.head

        if(pos == 1):
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            while(p != pos - 1):
                temp = temp.next
                p +=1 
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node

            if(new_node.next != None):
                new_node.next.prev = new_node

    def print(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
lobj = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

print("After appending : \n")
lobj.append(n1)
lobj.append(n2)
lobj.append(n3)
lobj.append(n4)

lobj.print()

n5 = Node(35)
print("After insertion : ")
lobj.insert(n5, 3)

lobj.print()