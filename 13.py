''' 
    5 4 3 2 1
    5 4 3 2
    5 4 3
    5 4
    5
'''

row = int(input("Enter the number of rows : "))

for i in range(row, 0, -1):
    for j in range(i, 0, -1):    
        print(j, end = " ")
    print()
        