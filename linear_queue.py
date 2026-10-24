# Linear Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LQueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, new_node):    # for other nodes
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:     # for the first node                          
            self.front = self.rear = new_node

    def display(self):
        temp = self.front
        while(temp != None):
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
que = LQueue()

que.enqueue(Node(10))
que.enqueue(Node(20))
que.enqueue(Node(30))
que.enqueue(Node(40))

que.display()