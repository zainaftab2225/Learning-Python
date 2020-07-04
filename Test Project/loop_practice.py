print()
print("Question 1")
for i in range(10):
    print("*", end=" ")
print()
print("Question 2")
for i in range(10):
    print("")
    for j in range(10):
        print("*", end="")
print()
print("Question 4")
for row in range(10):
    print("")
    for col in range(5):
        print("*", end="")
print()
print("Question 5")
for row in range(5):
    print("")
    for col in range(20):
        print("*", end=" ")
print()
print("Question 6")

for row in range(10):
    counter = 0
    print("")
    for col in range(10):
        print(counter, end=" ")
        counter += 1
print()
print("Question 7")

counter = 0
for row in range(10):
    print("")
    for col in range(10):
        print(counter, end=" ")
    counter += 1

print()
print("Question 8")

for row in range(10):
    print("")
    counter = 0
    for col in range(row+1):
        print(counter, end=" ")
        counter += 1

print()
print("Question 9")

index_col = 10
space_counter = 0
for row in range(10):
    print("")
    counter = 0
    for i in range(space_counter):
        print("  ", end="")
    for col in range(index_col):
        print(counter, end=" ")
        counter += 1

    index_col -= 1
    space_counter += 1

print()
print("Question 10")

counter = 1
for row in range(10):
    print("")
    print_counter = counter
    print(counter, end=" ")
    for col in range(10):

        counter += 1

print("Test")

for row in range(1, 10):
    for col in range(1, 10):
        if i*j < 10:
            print("   ", end=" ")
        print(row*col, end=" ")
    print("")

print()
print("Question 11")

for row in range(10):
    print("")
    counter = 1
    for col in range(row):
        print(counter, end="")
        counter += 1
    for col in range(row, 0, -1):
        print(row, end=" ")
