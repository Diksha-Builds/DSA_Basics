# Find the smallest and largest element

n = int(input("Enter number of elements : "))

arr = []

for i in range(n):
    num = int(input("Enter the element : "))
    arr.append(num)

max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if(arr[i] > max):
        max = arr[i]
    elif(arr[i] < min):
        min = arr[i]

print("Largest number is : ",max)
print("Smallest number is : ",min) 



