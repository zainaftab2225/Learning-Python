# Part 1

print("Part 1")

counter = 10
for row in range(10):
    print("")
    for col in range(row):
        print(counter, end=" ")
        counter += 1
print()
print()
print("Part 2")
print()

n = int(input("Enter n: "))

for x in range(n):
    print("o", end="")

print("")

for x in range(n):
    print("o", end="")
    for y in range(0, n-2):
        print(" ", end="")
    print("o")
for x in range(n):
    print("o", end="")
