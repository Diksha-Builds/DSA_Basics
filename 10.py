# Find the smallest, second smallest, largest & second largest number from the array

Arr = [10, 3, 45, 6, 8, 23, 42, 56, 30]

max = Arr[0]
min = Arr[0]

smin = Arr[0]
smax = Arr[0]

for i in Arr:
    if(i > max):
        smax = max
        max = i
    elif(i > smax and i != max):
        smax = i
    
    if(i < min):
        smin = min
        min = i
    elif(i < smin and i != smin):
        smin = i

print("Maximum : ",max)
print("Minimum : ",min)

print("Second Maximum : ",smax)
print("Second Minimum : ",smin)

    