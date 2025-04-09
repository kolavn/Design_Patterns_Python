rows=6
for i in range(rows):
    for j in range(rows-i):
        print(" ", end=" ")

    breakpoint = (2*i+1)/2
    for j in range(0, 2*i+1):
        ascii_value = 65 + j
        if j<=breakpoint:
            print(chr(ascii_value), end=" ")
        else:
            ascii_value = 65 + j ###############
            print(chr(ascii_value), end=" ")


    for j in range(rows-i):
        print(" ",end=" ")
    
    print(" ")