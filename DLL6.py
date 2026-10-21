''' Swap first and last node in DLL '''

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

    def delete(self, value):
        temp = self.head

        if temp.data == value:  # first node to delete
            self.head = self.head.next
            self.head.prev = None
        else:
            while(temp.data != value and temp != None):
                temp = temp.next
                if temp == None:
                    print("Value is not present in the list")
                    return

            temp.prev.next = temp.next  # last node
            if temp.next:   # Not the last node 
                temp.next.prev = temp.prev
            temp = None

    def countOccurrence(self, value):
        temp = self.head

        count = 0
        while temp != None:
            if temp.data == value:
                count += 1
            temp = temp.next

        print("The occurrence of the number : ",count)

    def swapNode(self):
        temp = node1 = self.head

        while temp.next != None:
            temp = temp.next 

        temp.next = node1.next
        node1.next = None 
        node1.prev = temp.prev
        temp = node1
        temp.prev = None

        self.head = temp

    def print(self):
        temp = self.head

        while(temp.next != None):
            temp = temp.next

        while temp != None: # reverse the node
            print(temp.data, end=" ")
            temp = temp.prev
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
lobj.append(Node(20))
lobj.append(Node(50))
lobj.append(Node(60))
lobj.append(Node(40))

lobj.print()

n5 = Node(35)
print("After insertion : ")
lobj.insert(n5, 3)

lobj.print()

lobj.delete(30)
lobj.print()

lobj.countOccurrence(20)

print("After swapping : ")
lobj.swapNode()
lobj.print()