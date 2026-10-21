class Node:     
    def __init__(self, val):         
        self.data = val         
        self.next = None 
 
class LinkedList:     
    def __init__(self):         
        self.head = None 
 
# 1. Create Linked-List append (Create nodes with positive and negative numbers) 
 
    def append(self, new_node):         
        if(self.head == None):             
            self.head = new_node 
        else: 
            temp = self.head 
 
            while(temp.next != None): 
                temp = temp.next 
 
            temp.next  = new_node 
 
# 2. Traverse and print the node values 
 
    def print(self): 
            temp = self.head 
     
            while(temp != None):                 
                print(temp.data, end=" ")                 
                temp = temp.next 
 
# 3. Insert node at a specific position 
 
    def insertAtPos(self, new_node, pos): 
        if(pos == 1): 
            new_node.next = self.head             
            self.head = new_node         
        else: 
            target = 1             
            temp = self.head 
 
            while(target != pos - 1 and temp.next != None): 
                temp = temp.next                 
                target += 1 
 
            new_node.next = temp.next             
            temp.next = new_node 
 
# 4. Delete the nodes having negative values 
 
    def delete(self):         
        temp = self.head         
        prev = None 
 
        while(temp != None):             
            if(temp.data < 0):                 
                if(prev == None): 
                    self.head = temp.next                 
                else: 
                    prev.next = temp.next 
            else: 
                prev = temp 
 
            temp = temp.next 
 
n1 = Node(-10) 
n2 = Node(-20) 
n3 = Node(30) 
n4 = Node(-40) 
 
lobj = LinkedList() 
 
print("After appending the nodes : ") 
lobj.append(n1) 
lobj.append(n2) 
lobj.append(n3) 
lobj.append(n4) 
 
lobj.print() 
 
print("\nAfter inserting a node at a specific position : ") 
lobj.insertAtPos(Node(25), 3) 
 
lobj.print() 
 
print("\nAfter deleting negative nodes : ") 
lobj.delete() 
 
lobj.print() 