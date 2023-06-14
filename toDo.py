import os

toDo = []

COLORS = {
    "red": "\033[1;31m",
    "white": "\033[0;1m",
    "blue": "\033[1;34m",
    "yellow": "\033[1;33m",
    "green": "\033[1;32m",
    "purple": "\033[1;35m",
    "light": "\033[0;2;3m",
    "reset": "\033[0m"
}

def colorChange(color):
    return COLORS.get(color, "")

def printList():
  print()
  print(f"{colorChange('reset')}{colorChange('blue')}Current List:")
  for userItem in toDo:
    print(f"{colorChange('reset')}{userItem}")
  print()
  
def findItem (userItem):
  changeItem = input(f"What would you like to replace {userItem} with\n")
  location = toDo.index(userItem)
  toDo.pop(location)
  toDo.insert(location, changeItem)

def intro ():
  title = "TO DO LIST"
  subtitle = "Welcome to your custom to do list"
  print(f"{colorChange('reset')}{colorChange('blue')}{title:^50}")
  print(f"{colorChange('light')}{subtitle:^50}")
  print()
  

def userInput():
  test = input(f"{colorChange('light')}Add/Remove/View/Edit: \n> ")
  os.system('clear')
  return test

counter = 0
while True:
  if counter == 0:
    intro()
    counter += 1
    
  test = userInput()
  
  if test == "add":
    os.system('clear')
    userItem = input(f"{colorChange('light')}What would you like to add?\n> ")
    toDo.append(userItem)
    printList()
    counter += 1
  
  
  elif test == "remove":
    if len(toDo) == 0:
      print("The list is empty")
      print("")
    else: 
      printList()
      userItem = input(f"{colorChange('light')}What would you like to remove? ")
      toDo.remove(userItem)
      printList()
      counter += 1

  elif test == "view":
    if len(toDo) == 0:
      print("The list is empty")
      print("")
    else:
      printList()
      counter += 1
    
  elif test == "edit":
    if len(toDo) == 0:
      print("The list is empty")
      print("")
    else:
      printList()
      userItem = input("What would you like to edit? ")
      location = findItem(userItem)
      print()
      printList()
      counter += 1

  elif test == "home":
    counter = 0
