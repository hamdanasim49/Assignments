class ListItem:
    def __init__(self, description):
        self.description = description
        self.done = False

    def printItem(self):
        if self.done:
            print("\u2705", self.description)
        else:
            print("\u2750", self.description)

    def changeMark(self):
        if self.done:
            self.done = False
        else:
            self.done = True

        return self.done

    def getDescription(self):
        return self.description


def printMenu():
    print("1 - Add item to list")
    print("2 - Remove item from list")
    print("3 - Mark done/Not done an item")
    print("4 - List all items")
    print("5 - Quit")


def findItem(ToDoList, description):
    index = -1
    for i in range(len(ToDoList)):
        if ToDoList[i].getDescription() == description:
            index = i
    return index


def removeItem(ToDoList):
    print("\nPlease enter the description of item to remove: ", end="")
    description = input()
    index = findItem(ToDoList, description)
    if index == -1:
        print("Sorry there was no item with this description")
    else:
        ToDoList.pop(index)
        print("*** Item has been removed successfully ***")


def ItemStatus(ToDoList):
    print("\nPlease enter the description of item to mark/unmark: ", end="")
    description = input()
    index = findItem(ToDoList, description)
    if index == -1:
        print("Sorry there was no item with this description")
    else:
        status = ToDoList[index].changeMark()
        if status:
            print("*** Item has been marked ***")
        else:
            print("*** Item has been unmared ***")


def main():
    ToDoList = []
    choice = " "
    while choice != "5":
        printMenu()
        choice = input("Please enter your choice (1-5): ")
        if choice == "5":
            print("Thank you for using the program")
        elif choice == "1":
            print("\nPlease enter the description of item to do: ", end="")
            description = input()
            obj = Listitem(description)
            ToDoList.append(obj)
            print("*** Item has been added to your to do list ***")
        elif choice == "2":
            removeItem(ToDoList)
        elif choice == "3":
            ItemStatus(ToDoList)
        elif choice == "4":
            print("Items in To do list are: ")
            for item in ToDoList:
                item.printItem()
        print()


main()
