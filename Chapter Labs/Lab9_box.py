def box(height, width):
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()


box(7, 5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3, 2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3, 10)  # Print a box 3 high, 10 across
