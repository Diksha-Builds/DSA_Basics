# Search an element

n = int(input("Enter number of elements : "))

arr = []

for i in range(n):
    num = int(input("Enter the element : "))
    arr.append(num)

s = int(input("Enter the element that you want to search : "))

iCount = 1

for i in range(n):
    if(arr[i] == s):
        print("The number is present at position",iCount)
    else:
        iCount += 1        
