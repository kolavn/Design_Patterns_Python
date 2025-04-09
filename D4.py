rows = 5
for i in range(rows):
    for j in range(0,rows-i):
        print(" ", end=" ")
    for j in range(0,2*i+1):
        print("*", end= " ")
    for j in range(0,rows-i):
        print(" ", end = " ")
    print(" ")

for i in range(rows+1):
    for j in range(0,i):
        print(" ", end=" ")
    for j in range((2*rows-(2*i-1)), 0 , -1):
        print("*", end= " ")
    for j in range(0,i):
        print(" ", end = " ")
    print(" ")