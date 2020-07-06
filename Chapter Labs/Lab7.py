

replay = "Y"
while replay == "Y":

    room_list = []
    room_item_list = []
    user_inventory = []
    # Room has elements: DESCRIPTION, NORTH, WEST, EAST, SOUTH, LIGHT_STATUS
    # Room 0: BEDROOM
    room = ["You are in the BEDROOM. \nYou see a door to the NORTH and a glass door to your EAST.",
            3, None, 1, None, True]
    room_list.append(room)

    # Room 1: SOUTH HALL
    room = ["You are in the SOUTH HALL. \nThe hall extends to the NORTH. \nYou also see a door to the WEST and a door to the EAST. ", 4, 0, 2, None, True]
    room_list.append(room)

    # Room 2: DINING ROOM
    room = ["You are in the DINING ROOM. \nYou see a connecting door to the NORTH and a door to the WEST.", 5, 1, None, None, True]
    room_list.append(room)

    # Room 3: LIVING ROOM
    room = ["You are in the LIVING ROOM. \nYou see a door to the EAST and a door to the SOUTH.",
            None, None, 4, 0, False]
    room_list.append(room)

    # Room 4: NORTH HALL
    room = ["You are in the NORTH HALL. \nYou see a balcony window to the NORTH, a door to the WEST and a door the EAST. \nThe hall also extends to the SOUTH.", 6, 3, 5, 1, True]
    room_list.append(room)

    # Room 5: KITCHEN
    room = ["You are in the KITCHEN. \nYou see a door to the WEST and a door to the SOUTH.",
            None, 4, None, 2, True]
    room_list.append(room)

    # ROOM 6: BALCONY
    room = ["You are in the BALCONY. \nYou can escape from the BALCONY by jumping NORTH. You see a door behind you to the SOUTH.", "END", None, None, 4, True]
    room_list.append(room)
    # ROOM 0: BEDROOM ITEMS
    room_items = ["WAX STATUE", "BATTERY"]
    room_item_list.append(room_items)

    # ROOM 1: SOUTH HALL ITEMS
    room_items = ["TORCH"]
    room_item_list.append(room_items)

    # ROOM 2: DINING ROOM ITEMS
    room_items = ["BRICK"]
    room_item_list.append(room_items)

    # ROOM 3: LIVING ROOM ITEMS
    room_items = ["MATCHBOX"]
    room_item_list.append(room_items)

    # ROOM 4: NORTH HALL ITEMS
    room_items = ["SWORD", "SHIELD", "SPECIAL RELIC"]
    room_item_list.append(room_items)

    # ROOM 5: KITCHEN
    room_items = ["MAP"]
    room_item_list.append(room_items)

    # ROOM 6: BALCONY
    room_items = ["ROPE"]
    room_item_list.append(room_items)

    user_inventory = []
    inventory_limit = 2
    done = False
    torch_status = False
    balcony_key = False
    current_room = 0
    while done is False:
        print("")
        print("-----------------------------------------------")
        print(room_list[current_room][0])
        print("-----------------------------------------------")
        print("A. Select to move.")
        print("B. Look around.")
        print("C. Take item.")
        print("D. Drop item.")
        print("E. Combine items.")
        print("F. Check inventory.")
        print("G. Open the map.")
        print("Q. Quit")
        user_main_choice = input("Enter your choice: ")

        # Quit Block
        if user_main_choice.upper() == "Q" or user_main_choice.upper() == "QUIT":
            done = True

        # Look Around Block
        elif user_main_choice.upper() == "B":
            print("Choice B selected.")
            if room_list[current_room][5] is True or torch_status is True:
                if len(room_item_list[current_room]):
                    print(room_item_list)
                    print("You look around the room and see :", room_item_list[current_room])
                else:
                    print("There is nothing important in this room.")
            else:
                print("It is too dark to look around the room.")

        # Take Item Block
        elif user_main_choice.upper() == "C":
            if room_list[current_room][5] is True or torch_status is True:
                print("You look around the room and see :", room_item_list[current_room])
                user_item_pickup_choice = input("Enter the name of the item you want to take: ")
                if len(user_inventory) < inventory_limit:
                    for item in room_item_list[current_room]:
                        print(item)
                        if item == user_item_pickup_choice.upper():
                            user_inventory.append(item)
                            print(item, " added to inventory.")
                            room_item_list[current_room].remove(item)
                            print(item, " removed from the room.")
                else:
                    print("Inventory full.")
            else:
                print("It is too dark to look around the room.")
        # Drop Item Block
        elif user_main_choice.upper() == "D":
            print("Option D")
            if len(user_inventory):
                print("Your inventory is:", user_inventory)
                user_item_drop_choice = input("Enter the name of the item you want to drop: ")
                for item in user_inventory:
                    print(item)
                    if item == user_item_drop_choice.upper():
                        user_inventory.remove(item)
                        print(item, " removed from inventory.")
                        room_item_list[current_room].append(item)
                        print(item, " added to the room.")

                print(user_inventory)
                print(room_item_list[current_room])
            else:
                print("Inventory is empty.")

        # Combine Items
        elif user_main_choice.upper() == "E":
            print("Option E")
            if len(user_inventory) == 2:
                battery_flag = False
                torch_flag = False
                statue_flag = False
                matchbox_flag = False
                for item in user_inventory:
                    if item == "BATTERY":
                        battery_flag = True
                    if item == "TORCH":
                        torch_flag = True
                    if item == "WAX STATUE":
                        statue_flag = True
                    if item == "MATCHBOX":
                        matchbox_flag = True

                if battery_flag == True and torch_flag == True:
                    print("Combining possible.")
                    user_inventory = []
                    user_inventory.append("WORKING TORCH")
                    torch_status = True

                if statue_flag == True and matchbox_flag == True:
                    print("Combining possible2.")
                    user_inventory = []
                    user_inventory.append("BALCONY KEY")
                if len(user_inventory) == 1:
                    print("Items combined.")
                    print(user_inventory)
                else:
                    print("Nothing to combine.")
            else:
                print("Nothing to combine.")

        # Inventory Block
        elif user_main_choice.upper() == "F":
            print("Your inventory is: ", user_inventory)

        # Map Block
        elif user_main_choice.upper() == "G":
            map_flag = False
            for item in user_inventory:
                if item == "MAP":
                    map_flag = True
            if map_flag == True:
                print("   +-------------+----------------+")
                print("   |             |   BALCONY      |")
                print("   |             |                |")
                print("   |   LIVING    +--------------+-+----------------+")
                print("   |   ROOM      |              |                  |")
                print("   |             |              |                  |")
                print("   |             |              |     KITCHEN      |")
                print("   |             |              |                  |")
                print("   |             |              |                  |")
                print("   |             |              |                  |")
                print("+--+-------------+              +------------------+")
                print("|                |     HALL     |                  |")
                print("|                |              |                  |")
                print("|                |              |                  |")
                print("|     BEDROOM    |              |  DINING ROOM     |")
                print("|                |              |                  |")
                print("|                |              |                  |")
                print("|                |              |                  |")
                print("|                |              |                  |")
                print("+----------------+--------------+------------------+")
            else:
                print("You do not have a map.")
            # Movement Block
        elif user_main_choice.upper() == "A":
            user_movement_choice = input("Where do you want to go? ")
            if user_movement_choice.upper() == "N" or user_movement_choice.upper() == "NORTH":
                next_room = room_list[current_room][1]
                balcony_flag = False
                for item in user_inventory:
                    if item == "BALCONY KEY":
                        balcony_flag = True
                if (next_room is None):
                    print()
                    print("You can't go that way.")
                    print(next_room)
                elif (next_room == "END"):
                    print("You have managed to escape the dungeon!")
                    done = True
                elif (next_room == 6 and balcony_flag is False):
                    print("You need the BALCONY KEY to enter the BALCONY.")
                elif (next_room == 6 and balcony_flag is True):
                    current_room = next_room
                else:
                    current_room = next_room
                    print("You are now in ", current_room)
            elif user_movement_choice.upper() == "W" or user_movement_choice.upper() == "WEST":
                next_room = room_list[current_room][2]
                if (next_room is None):
                    print()
                    print("You can't go that way.")
                else:
                    current_room = next_room
                    print("You are now in ", current_room)
            elif user_movement_choice.upper() == "E" or user_movement_choice.upper() == "EAST":
                next_room = room_list[current_room][3]
                if (next_room is None):
                    print()
                    print("You can't go that way.")
                else:
                    current_room = next_room
            elif user_movement_choice.upper() == "S" or user_movement_choice.upper() == "SOUTH":
                next_room = room_list[current_room][4]
                if (next_room is None):
                    print()
                    print("You can't go that way.")
                else:
                    current_room = next_room
                    print("You are now in ", current_room)
            else:
                print()
                print("That isn't a direction. Choose from North, West, East or South.")
        # Wrong Choice Block
        else:
            print("Wrong choice, try again!")
    user_replay_choice = input("Do you want to replay? (Y/N)")
    replay = user_replay_choice.upper()
