import random
import time

replay = "Y"
while replay == "Y":
    print("------------------")
    print("      Camel      ")
    print("------------------")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.")
    user_distance = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    canteen_drinks = 3
    done = False

    while done is False:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("Enter your choice: ")
        print("")
        print("")
        if user_choice.upper() == "Q":
            done = True
        elif user_choice.upper() == "E":
            print("----------------------------------------------------------")
            print("Miles travelled: ", user_distance)
            print("Drinks in canteen: ", canteen_drinks)
            print("The natives are ", (user_distance - native_distance), " miles behind you!")
            print("----------------------------------------------------------")
            print("")
            print("")
        elif user_choice.upper() == "D":
            camel_tiredness = 0
            native_increase = random.randrange(7, 15)
            native_distance = native_distance + native_increase
            print("----------------------------------------------------------")
            print("The camel is happy now and free from tiredness.")
            print("----------------------------------------------------------")
            print("")
            print("")
        elif user_choice.upper() == "C":
            user_increase = random.randrange(10, 21)
            user_distance = user_distance + user_increase
            thirst += 1
            camel_tiredness = camel_tiredness + random.randrange(1, 4)
            native_increase = random.randrange(7, 15)
            native_distance = native_distance + native_increase
            print("----------------------------------------------------------")
            print("You travelled ", user_increase, " miles.")
            print("----------------------------------------------------------")
            print("")
            print("")
        elif user_choice.upper() == "B":
            user_increase = random.randrange(5, 13)
            thirst += 1
            camel_tiredness += 1
            native_increase = random.randrange(7, 15)
            native_distance = native_distance + native_increase
            print("----------------------------------------------------------")
            print("You travelled ", user_increase, " miles.")
            print("----------------------------------------------------------")
            print("")
            print("")
        elif user_choice.upper() == "A":
            if canteen_drinks > 0:
                canteen_drinks -= 1
                thirst = 0
                print("----------------------------------------------------------")
                print("You drank from the canteen. Remaining drinks: ", canteen_drinks)
                print("----------------------------------------------------------")
            else:
                print("----------------------------------------------------------")
                print("Out of drinks.")
                print("----------------------------------------------------------")
            print("")
            print("")
        else:
            print("----------------------------------------------------------")
            print("Wrong choice, try again!")
            print("----------------------------------------------------------")
            print("")
            print("")

        if thirst > 6:
            print("----------------------------------------------------------")
            print("You died of thirst!")
            print("----------------------------------------------------------")
            print("")
            print("")
            done = True
        elif thirst > 4:
            print("----------------------------------------------------------")
            print("You are thirsty.")
            print("----------------------------------------------------------")
            print("")
            print("")

        if camel_tiredness > 8:
            print("----------------------------------------------------------")
            print("Your camel died!")
            print("----------------------------------------------------------")
            print("")
            print("")
            done = True
        elif camel_tiredness > 5:
            print("----------------------------------------------------------")
            print("Your camel is getting tired, it may be a good idea to rest for the night.")
            print("----------------------------------------------------------")
            print("")
            print("")

        if native_distance >= user_distance:
            print("----------------------------------------------------------")
            print("The natives caught up and killed you!")
            print("----------------------------------------------------------")
            print("")
            print("")
            done = True
        elif (user_distance-native_distance) < 15:
            print("The natives are getting close!")

        if not done and user_distance >= 200:
            done = True
            print("----------------------------------------------------------")
            print("You've managed to evade the natives. The camel is yours!")
            print("----------------------------------------------------------")
            print("")
            print("")

    print("---------------")
    print(" Game Finished")
    print("---------------")
    user_replay = input("Do you want to replay? (Y/N) ")
    replay = user_replay.upper()
