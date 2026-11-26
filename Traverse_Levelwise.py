#BST using Linked List

class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
       
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subtree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return

        arr = []
        cnt = 0     # For counting visited node
        arr.append(rt)

        while cnt < len(arr):
            temp = arr[cnt]
            cnt += 1
            print(temp.data, end=" ")

            if temp.left:
                arr.append(temp.left)

            if temp.right:
                arr.append(temp.right)

b1=BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\nInorder: ")
b1.inorder(b1.root)

print("\nLevel Order: ")
b1.level_order(b1.root)