def find(search_list, key):
    for i in range(len(search_list)):
        if search_list[i] == key:
            print("Found ", key, " at position ", i)


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)
