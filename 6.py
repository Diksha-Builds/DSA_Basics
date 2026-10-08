# Remove duplicate elements -> Pending

n = int(input("Enter the number of elements : "))

arr = []

for i in range(n):
    num = int(input("Enter the element : "))
    arr.append(num)

comp = arr[n-1]
brr = []

for i in range(n):
    if(arr[i] == comp):
        print("")
        comp-=1
    else:
        brr.append(arr[i])

print(brr)

