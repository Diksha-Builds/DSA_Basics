# Count even and odd numbers

n = int(input("Enter number of elements : "))

arr = []

for i in range(n):
    num = int(input("Enter the element : "))
    arr.append(num)

evenCount = 0
oddCount = 0

for i in range(n):
    if(arr[i] % 2 == 0):
        evenCount += 1
    else:
        oddCount += 1

print("Total odd numbers are : ",oddCount)
print("Total even numbers are : ",evenCount)