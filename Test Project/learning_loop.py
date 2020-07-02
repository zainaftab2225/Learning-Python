import random

'''
Looping Practice
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done")

a = 0
for i in range(10):
    a = a + 1
print(a)


a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)


value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)
'''
'''
for i in range(10):
    print("Zain")
print("Done")


for i in range(4):
    print("Red")
    print("Gold")

for i in range(2, 101, 2):
    print(i)

counter = 10
while counter > -1:
    print(counter)
    counter = counter - 1
print("Blast off")


print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = float(input("Enter a number: "))
    total = total + x
print("The total is:", total)
'''
'''
Random Practice
number = random.randrange(1, 11)
print(number)

number = random.random() * 9 + 1
print(number)
'''

'''
total = 0
positive_entries = 0
negative_entries = 0
zero_entries = 0
for i in range(7):
    x = float(input("Enter your number: "))
    if x == 0:
        zero_entries += 1
    elif x > 0:
        positive_entries += 1
    else:
        negative_entries += 1
    total = total + x
print("The total is: ", total)
print("Positive: ", positive_entries)
print("Negative: ", negative_entries)
print("Zeroes: ", zero_entries)
'''
'''
total_heads = 0
total_tails = 0
for i in range(50):
    flip = random.randrange(0, 2)
    if flip == 0:
        print("Heads")
        total_heads += 1
    else:
        print("Tails")
        total_tails += 1
print("Total Heads: ", total_heads)
print("Total Tails: ", total_tails)
'''

'''
print("0. Rock")
print("1. Paper")
print("2. Scissors")
user_number = int(input("Enter your choice: "))
number = random.randrange(0, 3)
if number == 0:
    print("Computer chose Rock!")
elif number == 1:
    print("Computer chose Paper!")
else:
    print("Computer chose Scissors!")

if user_number == 0 and number == 1:
    print("Result: Paper beats Rock, AI won")
elif user_number == 0 and number == 2:
    print("Result: Rock beats Scissors, YOU won")
elif user_number == 1 and number == 0:
    print("Result: Paper beats Rock, YOU won")
elif user_number == 1 and number == 2:
    print("Result: Scissors cut Paper, AI won")
elif user_number == 2 and number == 0:
    print("Result: Rock beats Scissors, AI won")
elif user_number == 2 and number == 1:
    print("Result: Scissors beat Paper, YOU won")
else:
    print("Result: TIE")
'''

number = random.randrange(7, 15)
print(number)
