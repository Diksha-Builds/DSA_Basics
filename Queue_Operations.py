class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def Enqueue(self, val):
        new_node = Node(val)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(val, "enqueued into the queue")

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        temp = self.front
        print("Dequeued Element : ",temp.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    def Display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue contains...")

            temp = self.front

            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")

    def ReverseUsingStack(self):
        stack = []

        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = None
        self.rear = None

        while stack:
            self.Enqueue(stack.pop())

        print("Queue reversed successfully")

    def Merge(self, queue2):
        merged_queue = Queue()

        temp = self.front

        while temp:
            merged_queue.Enqueue(temp.data)
            temp = temp.next

        temp = queue2.front

        while temp:
            merged_queue.Enqueue(temp.data)
            temp = temp.next

        return merged_queue

    def IsIdentical(self, queue2):
        temp1 = self.front
        temp2 = queue2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None

q1 = Queue()
q2 = Queue()

print("\nEnque Operation : ")
q1.Enqueue(10)
q1.Enqueue(20)
q1.Enqueue(30)

q1. Display()

print("\nDequeue Operation : ")
q1.Dequeue()
q1.Display()

print("\nReverse Queue using Stack : ")
q1.ReverseUsingStack()
q1.Display()

print("\nSecond Queue : ")
q2.Enqueue(40)
q2.Enqueue(50)
q2.Enqueue(60)

q2.Display()

print("\nMerge two queues : ")
q3 = q1.Merge(q2)

print("Merged Queue : ")
q3.Display()

print("\nCheck if queues are identical : ")

if q1.IsIdentical(q2):
    print("Both queues are identical")

else:
    print("Both queues are not identical")