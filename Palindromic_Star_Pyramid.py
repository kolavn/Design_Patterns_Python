# Palindromic Star Pyramid Program

n = int(input("Enter number of rows: "))

# Upper half (including middle row)
for i in range(1, n + 1):
    # Print leading spaces
    for space in range(n - i):
        print(" ", end="")

    # Print stars with space
    for star in range(i):
        print("*", end=" ")

    print()  # New line

# Lower half
for i in range(n - 1, 0, -1):
    # Print leading spaces
    for space in range(n - i):
        print(" ", end="")

    # Print stars with space
    for star in range(i):
        print("*", end=" ")

    print()  # New line
