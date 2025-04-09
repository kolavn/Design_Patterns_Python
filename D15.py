rows=5
for i in range(rows):
    for j in range(0,i+1):
        ascii_value = 65 + i
        print(chr(ascii_value), end=" ")
       
    for j in range(i):
        print(" ", end= " ")
    print("")