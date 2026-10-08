num = int(input("Enter the num : "))

mid = (num+1) / 2

for i in range(num):
    for j in range(num):
        if(j == mid or i == mid):
            print('*', end = ' ')
        else :
            print(" ", end = ' ')
    print()
