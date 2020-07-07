import random


def average_list(avg_list):
    sum = 0
    list_length = len(avg_list)
    for i in range(list_length):
        sum = sum + avg_list[i]
    average = sum/list_length
    return average


def count_list(list_to_count, key):
    counter = 0
    for i in range(len(list_to_count)):
        if list_to_count[i] == key:
            counter += 1
    return counter


def create_list(size):
    final_list = []
    for i in range(size):
        random_number = random.randrange(1, 7)
        final_list.append(random_number)
    return final_list


my_list = create_list(10000)
counter1 = count_list(my_list, 1)
print("1 appears ", counter1, " times.")
counter2 = count_list(my_list, 2)
print("2 appears ", counter2, " times.")
counter3 = count_list(my_list, 3)
print("3 appears ", counter3, " times.")
counter4 = count_list(my_list, 4)
print("4 appears ", counter4, " times.")
counter5 = count_list(my_list, 5)
print("5 appears ", counter5, " times.")
counter6 = count_list(my_list, 6)
print("6 appears ", counter6, " times.")
print("Total count is ", counter1+counter2+counter3+counter4+counter5+counter6)
average = average_list(my_list)
print("The average is ", average)
