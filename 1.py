# Calculate Array Sum

num = int(input("Enter number of elements : "))

arr = []

for i in range(num):
    n = int(input("Enter element : "))
    arr.append(n)

sum = 0

for i in range(num):
    sum = sum + arr[i]

print("Sum of array elements : ",sum)
