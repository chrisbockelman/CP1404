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
            change_type()
            print("Item marked as completed")
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()

#Displays list, for required, input = 'r', or for completed, input = 'c'
def display_list(input):
    file = open("items.csv", "r")
    count = 1
    for line_string in file:
        if line_string[-1] == input:
            item, price, priority, tag = line_string.split(",")
            print("{}. {}\t ${:>5} ({})".format(count,item,price, priority))
            count += 1
    file.close()

#Adds new item to the list

#FINISH THIS FUNCTION
def add_item():
    file = open("items.csv", "a+")
    item = input("Item name: ")
    if item == "":
        print("Input cannot be blank")
        item = input("Item name: ")
    try:
        price = float(input("Price: $"))
        if price < 0:
            print("Price must be >= $0")
    except ValueError:
        print("Please enter a valid number")
        price = float(input("Price: $"))
    file.close()


#Changes required tag, 'r' to completed tag, 'c'
def change_type():
    file = open("items.csv", "a+")
    count = 1
    for line_string in file:
        item, price, priority, tag = line_string.split(",")
        print("{}. {}\t ${:>5} ((})".format(count, item, price, priority))
        count += 1
    try:
        choice = int(input("Enter the number of an item to mark as completed: "))

    except ValueError:
        print("Not a valid number")
        choice = int(input("Enter the number of an item to mark as complete:"))
    file.close()

main()
