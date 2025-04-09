rows=5
for i in range(rows):
    for j in range(rows-i):
        ascii_value = 65 + j
        print(chr(ascii_value), end=" ")
        # num = num+1
    for j in range(rows-i):
        print(" ", end= " ")
    print("")