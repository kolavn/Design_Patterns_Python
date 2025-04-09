rows = 6
for i in range(rows):
    for j in range(rows-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(j, end = " ")
    print(" ")