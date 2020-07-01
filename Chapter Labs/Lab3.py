score = 0
TOTAL = 5
correct = "Correct!"
incorrect = "Incorrect."
print("Quiz Time!")


answer_1 = float(input("How many games are there in The Last of Us franchise?"))
if answer_1 == 2:
    print(correct)
    score = score + 1
else:
    print(incorrect)

answer_2 = float(input("What is 3 x (2 - 1)?"))
if answer_2 == 3:
    print(correct)
    score = score + 1
else:
    print(incorrect)

answer_3 = float(input("What is 3 x 2 - 1?"))
if answer_3 == 5:
    print(correct)
    score = score + 1
else:
    print(incorrect)

answer_4 = float(input("Who is the better character? \n 1. Abby \n 2. Ellie"))
if answer_4 == 2:
    print(correct)
    score = score + 1
else:
    print(incorrect)

answer_5 = float(input(
    "Who is on the front of a one dollar bill? \n1. George Washington\n2. Abraham Lincoln \n3. John Adams \n4. Thomas Jefferson"))

if answer_5 == 1:
    print(correct)
    score = score + 1
else:
    print(incorrect)

percentage = (score/5)*100
print("Congratulations, you got ", score, " answers right.")
print("That is a score of ", percentage, " percent.")
