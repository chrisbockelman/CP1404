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
            print("Required list")
        elif choice == "C":
            print("Completed list")
        elif choice == "A":
            print("Add list")
        elif choice == "M":
            print("Mark item as complete")
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()

main()
#file = open(items.csv, a+)
