#Shopping List 1.0 - by Chris Bockelman
#Fair warning, items.csv randomly stops
from operator import itemgetter
import os, sys
MENU = "\nMenu:\n(R)equired items\n(C)ompleted items\n(A)dd item\n(M)ark item as completed\n(Q)uit"

def main():
    print("Shopping List 1.0 - by Chris Bockelman")

    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "R":
            print("Required items:")
            display_list("r")
        elif choice == "C":
            print("Completed items:")
            display_list("c")
        elif choice == "A":
            add_item()
        elif choice == "M":
            display_list("r")
            change_type()
            print("Item marked as completed")
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()

#Displays list, for required: input = 'r', or for completed: input = 'c'
def display_list(menuChoice):
    items = []
    file = open("items.csv", "r")
    count = 1
    for line_string in file:
        itemName, price, priority, tag = line_string.strip().split(", ")
        items.append([itemName,float(price),int(priority),tag])

    items.sort(key=itemgetter(0, 2))

    for item in items:
        if item[3] == menuChoice:
            print("{}. {:20} ${:>6.2f} ({})".format(count, item[0], item[1], item[2]))
            count += 1

    file.close()

#Adds new item to the list

def add_item():
    file = open("items.csv", "a+")
    itemName = input("Item name: ")

    #Add item name
    if itemName == "":
        print("Input cannot be blank")
        itemName = input("Item name: ")


    #Add item price
    try:
        price = float(input("Price: $"))
        if price < 0:
            print("Price must be >= $0")
            price = float(input("Price: $"))

    except ValueError:
        print("Please enter a valid number")
        price = float(input("Price: $"))

    #Add item priority
    try:
        priority = int(input("Priority (1 - High, 3 - Low): "))
        if priority >= 1 and priority <= 3:
            priority = priority
        else:
            priority = int(input("Please enter either 1, 2, or 3: "))

    except ValueError:
        priority = int(input("Please enter either 1, 2, or 3: "))


    print("{}, {}, {}, r".format(itemName.capitalize(), price, priority), file=file)
    print("{} has been added to the list.".format(itemName.capitalize()))

    file.close()


#Changes required tag, 'r' to completed tag, 'c'
def change_type():
    file = open("items.csv", "r")
    dict = {}
    countList = []
    count = 1

    for line_str in file:
        itemName, price, priority, tag = line_str.strip().split(', ')
        dict[count] = [itemName, price, priority, tag]
        countList.append(count)
        count += 1

    valid_input = False
    while not valid_input:
        try:
            choice = int(input("Enter the number of an item to mark as completed:"))
            valid_input = True

            while choice not in countList:
                print("Invalid input")
                choice = int(input("Enter the number of an item to mark as completed:"))
            count = choice
            dict[count][3] = "c"

            file.close()
            file = open('items.csv', 'w')
            for value in dict.values():
                tag = value[3]
                priority = value[2]
                price = value[1]
                itemName = value[0]
                print("{}, {}, {}, {}".format(itemName.capitalize, price, priority, tag), file=file)

        except ValueError:
            print("Input is invalid")
            continue


#TODO Write onto file without overwriting everything

    file.close()
    file = open('items.csv', 'w')

    print(dict)



    file.close()

main()