class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def Push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def Pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped Element : ",temp.data)
            self.top = self.top.next
            temp = None

    def Print(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack contains...")
            temp = self.top

            while temp:
                print(temp.data)
                temp = temp.next

    def ReverseString(self, string):
        temp = Stack()

        for char in string:
            temp.Push(Node(char))

        reversed_string = ""

        while not temp.isEmpty():
            reversed_string += temp.top.data
            temp.top = temp.top.next

        return reversed_string

    def ReverseStack(self, new_stack):
        temp = self.top

        while temp:
            new_stack.Push(Node(temp.data))
            temp = temp.next

sobj1 = Stack()
sobj2 = Stack()

sobj1.Push(Node(11))
sobj1.Push(Node(21))
sobj1.Push(Node(51))
sobj1.Push(Node(101))
sobj1.Push(Node(111))


print("\nOriginal Stack : ")
sobj1.Print()

print("\nPop Operation : ")
sobj1.Pop()
sobj1.Print()

string = "Diksha"

reversed_string = sobj1.ReverseString(string)

print("\nOriginal String : ",string)
print("Reversed String : ",reversed_string)

print("\nReversed Stack using another stack : ")

sobj1.ReverseStack(sobj2)
sobj2.Print()