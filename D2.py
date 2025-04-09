rows = 5
for i in range(rows):
    for j in range(0,2*i+1):
        print("*", end= " ")
    for j in range(0,rows-i):
        print(" ", end = " ")
    print(" ")

