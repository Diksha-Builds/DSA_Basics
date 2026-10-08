row = int(input("Enter number of rows : "))
col = int(input("Enter number of columns : "))

for i in range(row):
    for j in range(col):
        if(j % 2 == 0):
            print("0 1", end = " ")
        else:
            print("1 0", end = " ")
    print("\n")