rows=5
num = 1
for i in range(rows):
    for j in range(i):
        print(num,end=" ")
        num = num+1
    for j in range(rows-i):
        print(" ", end= " ")
    print("")
