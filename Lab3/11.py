rows=int(input("Enter number of rows: "))
col=int(input("Enter number of Coloumns: "))
array_2d = [[0 for _ in range(col)] for _ in range(rows)]
# list1=[[rows][col]]
for i in range(rows):
    for j in range(col):
        array_2d[i][j]=i*j
print(array_2d)
