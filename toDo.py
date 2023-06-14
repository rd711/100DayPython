import os

toDo = []

def colorChange(color):
    if color == "red":
        return ("\033[1;31m")
    elif color == "white":
        return ("\033[0;1m")
    elif color == "blue":
        return ("\033[1;34m")
    elif color == "yellow":
        return ("\033[1;33m")
    elif color == "green":
        return ("\033[1;32m")
    elif color == "purple":
        return ("\033[1;35m")
    elif color == "light":
        return ("\033[0;2;3m")
    elif color == "reset":
        return ("\033[0m")

def printList():
  print()
  if len(toDo) == 0:
      print("The list is empty")
      print("")
  else:
    print(f"{colorChange('reset')}{colorChange('blue')}Current List:")
    for userItem in toDo:
        print(f"{colorChange('reset')}{userItem}")
    print()

def findItem(userItem):
    changeItem = input(f"What would you like to replace {userItem} with\n> ")
    location = toDo.index(userItem)
    toDo.pop(location)
    toDo.insert(location, changeItem)

def intro():
    title = "TO DO LIST"
    subtitle = "Welcome to your custom to do list"
    print(f"{colorChange('reset')}{colorChange('blue')}{title:^50}")
    print(f"{colorChange('light')}{subtitle:^50}")
    print()
    printList()

def userInput():
    if counter >= 1 :
        test = input(f"{colorChange('light')}Add/Remove/View/Edit or Home: \n> ").lower()
    else:
        print(f"{colorChange('reset')}{colorChange('blue')}Get started with the commands below")
        test = input(f"{colorChange('light')}Add/Remove/View/Edit: \n> ").lower()
    os.system('clear')
    return test

counter = 0
while True:
    if counter == 0:
        intro()

    test = userInput()

    if test == "add":
        counter += 1
        os.system('clear')
        userItem = input(f"{colorChange('light')}What would you like to add?\n> ")
        toDo.append(userItem)
        printList()
        

    elif test == "remove":
        if len(toDo) == 0:
            print("The list is empty")
            print("")
        else:
            counter += 1
            printList()
            userItem = input(f"{colorChange('light')}What would you like to remove? ")
            toDo.remove(userItem)
            printList()
            

    elif test == "view":
        if len(toDo) == 0:
            print("The list is empty")
            print("")
        else:
            counter += 1
            printList()
            

    elif test == "edit":
        if len(toDo) == 0:
            print("The list is empty")
            print("")
        else:
            counter += 1
            printList()
            userItem = input(f"{colorChange('light')}What would you like to edit?\n> ")
            location = findItem(userItem)
            os.system('clear')
            printList()
            

    elif test == "home":
        counter = 0
