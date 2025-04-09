rows = 6
for i in range(rows):
    for j in range(0,2*i+1):
        print("*", end= " ")
    for j in range(0,rows):
        print(" ", end = " ")
    print(" ")

for i in range(rows):
    for j in range(0,2*rows-(2*i+1)-2):
        print("*", end= " ")
    for j in range(0,rows):
        print(" ", end = " ")
    print(" ")