item = [10, 20, 30, 40, 50]


item.append(100)

for x in item:
    print(x)

item[5] = 200

for x in item:
    print(x)

print(chr(ord("X")))


# Create an empty associative array
# (Note the curly braces.)
x = {}

# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

# Fetch and print an item
print(x["fred"])

my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)
