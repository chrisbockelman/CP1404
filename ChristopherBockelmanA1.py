#Shopping List 1.0 - by Chris Bockelman


from operator import itemgetter

def main():
    print("Shopping List 1.0 - by Chris Bockelman")
    MENU = "\nMenu:\n(R)equired items\n(C)ompleted items\n(A)dd item\n(M)ark item as completed\n(Q)uit"
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "R":
            print("Required items:")
            display_list(" r")
        elif choice == "C":
            print("Completed items:")
            display_list(" c")
        elif choice == "A":
            add_item()
        elif choice == "M":
            display_list(" r")
            change_type()
            print("Item marked as completed")
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()

"""Displays list, for required: input = 'r', or for completed: input = 'c'
pseudocode:
open items list, file, set count to 1
read lines from file and add to list
sort lines by priority
if final element of list equals input,
    print, add one to count
else ignore line
close file"""
def display_list(menuChoice):
    items = []
    totalPrice = []
    with open("items.csv") as file:
        count = 1
        for line_string in file:
            item, price, priority, tag = line_string.strip().split(',')
            items.append([item, float(price), int(priority), tag])
        items.sort(key=itemgetter(2))

        for item in items:
            if item[3] == menuChoice:
                totalPrice.append(float(item[1]))
                print("{}. {:20} ${:>6.2f} ({})".format(count, item[0].capitalize(), item[1], item[2]))
                count += 1
        print("The total price is ${:.2f}.".format(sum(totalPrice)))


"""Adds new item to the list
pseudocode:
open file
get valid item name
get valid item price
get valid priority
append name, price, priority, 'r' to file
close file
"""
def add_item():
    file = open("items.csv", "a+")
    itemName = input("Item name: ")

    #Add item name
    if itemName == "":
        print("Input cannot be blank")
        itemName = input("Item name: ")


    #Add item price
    valid_input = False
    while not valid_input:
        try:
            price = float(input("Price: $"))
            valid_input = True
            if price < 0:
                print("Price must be >= $0")
                price = float(input("Price: $"))

        except ValueError:
            print("Please enter a valid number")
            continue

    #Add item priority
    valid_input = False
    while not valid_input:
        try:
            priority = int(input("Priority (1 - High, 3 - Low): "))
            valid_input = True
            if priority >= 1 and priority <= 3:
                priority = priority
            else:
                priority = int(input("Please enter either 1, 2, or 3: "))

        except ValueError:
            print("Invalid input")
            continue


    print("{}, {}, {}, r".format(itemName, price, priority), file=file)
    print("{} has been added to the list.".format(itemName.capitalize()))

    file.close()


"""Changes required tag, 'r' to completed tag, 'c'
pseudocode:
open file, dictionary, count list, set count to one
read lines from file
add count as key to dictionary and add line as a list as value
add count to count list and increase count
get input
if input is in count list,
    change count to input
    edit last element in value of count to 'c'
    remove element from every value and write to file
close file"""
def change_type():
    file = open("items.csv", "r")
    dict = {}
    countList = []
    count = 1

    for line_str in file:
        itemName, price, priority, tag = line_str.strip().split(',')
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
                print("{}, {}, {}, {}".format(itemName, price, priority, tag), file=file)

        except ValueError:
            print("Input is invalid")
            continue
    file.close()

main()