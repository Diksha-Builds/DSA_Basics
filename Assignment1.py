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

    def insertAtPos(self, new_node, pos):

        iCount = self.count()

        if(pos < 1 or pos > iCount + 1):
            print("Invalid Position")
            return

        if(pos == 1):
            new_node.next = self.head
            self.head = new_node
        elif(pos == iCount + 1):
            self.append(new_node)
        else:
            target = 1
            temp = self.head

            while(target != pos - 1 and temp.next != None):
                temp = temp.next
                target += 1
            new_node.next = temp.next
            temp.next = new_node

    def findMiddle(self):
        if(self.head == None):
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        print("Middle element is : ",slow.data)

    def deleteNode(self, value):
        temp = self.head
        prev = None

        if(temp.data == value):
            self.head = self.head.next
            return

        while(temp != None):
            if(temp.data == value):
                break
            else:
                prev = temp
                temp = temp.next

        if(temp == None):
            print("Value is not present in the list")
            return

        prev.next = temp.next
        temp = None

    def reverse(self):
        curr = self.head
        prev = None

        while(curr):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    def sumConsecutive(self):
        temp = self.head
        iSum = 0

        while(temp != None and temp.next != None):
            iSum = temp.data + temp.next.data
            print(iSum)
            temp = temp.next

    def count(self):
        temp = self.head
        iCount = 0

        while(temp != None):
            iCount+=1
            temp = temp.next

        return iCount

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

iRet = lobj.count()
print("Total no. of nodes : ",iRet)

nobj4 = Node(35)

print("Insertion of a node at a specific position : ")
lobj.insertAtPos(nobj4, 4)

lobj.print()

iRet = lobj.count()
print("Total no. of nodes : ",iRet)

lobj.findMiddle()

lobj.deleteNode(35)

print("After deleting a node : ")
lobj.print()

iRet = lobj.count()
print("Total no. of nodes : ",iRet)

lobj.reverse()
lobj.print()

print("Sum of two consecutive numbers : ")
lobj.sumConsecutive()