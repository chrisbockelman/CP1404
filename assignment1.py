"""Shopping List 1.0 - by Chris Bockelman

Pseudocode:
def main:
    display menu
    get choice
    while choice is not 'q'
        if choice is r:
            list required items
        elif choice is 'c':
            list complete items
        elif choice is 'a':
            add new item
        elif choice is 'm':
            mark item as complete
        else:
            display error message
        display menu
        get choice
    goodbye message
"""

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

#Displays list, for required, input = 'r', or for completed, input = 'c'
#TODO Break list into individual parts for output and add price. STOP DISPLAYING WATCH PRICE/PRIORITY, SORT BY PRIORITY
def display_list(input):
    items = []
    file = open("items.csv", "r")
    count = 1
    for line_string in file:
        item, price, priority, tag = line_string.strip().split(",")
        items.append([item,float(price),priority,tag])

    for item in items:
        if item[3] == input:
            print("{}. {}\t ${:>5.2} ({})".format(count, item, price, priority))
            count += 1

    file.close()

#Adds new item to the list

def add_item():
    file = open("items.csv", "a+")
    name = input("Item name: ")

    #Add item name
    if name == "":
        print("Input cannot be blank")
        name = input("Item name: ")


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


    print("{},{},{},r".format(name.capitalize(), price, priority), file=file)

    file.close()


#Changes required tag, 'r' to completed tag, 'c'
#FINISH THIS FUNCTION
#TODO Figure out choice option, infinite nested if?
def change_type():
    items = []
    file = open("items.csv", "a+")
    count = 1
    countList = []
    for line_string in file:
        item, price, priority, tag = line_string.strip().split(",")
        items.append([item, float(price), priority, tag, count])
        countList.append(count)
        count += 1

    try:
        choice = int(input("Enter the number of an item to mark as completed: "))
        if choice in countList:
            for item in items:
                if items[-1] is choice:
                    items[0][3] = "c"

    except ValueError:
        print("Not a valid number")
        choice = int(input("Enter the number of an item to mark as complete:"))
    file.close()

main()
