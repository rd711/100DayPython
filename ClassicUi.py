import os 
import time
exit = "n"

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
    return ("\033[0;2;3;33m")


def musicApp():
  os.system("clear")
  appTitle = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}MUSIC APP {colorChange('blue')}={colorChange('white')}={colorChange('red')}="
  prev = "PREV"
  next = "NEXT"
  pause = "PAUSE"

  print(f" {appTitle:>35}")
  print(f"\t{colorChange('white')}Radio Gaga")
  print(f"\t{colorChange('yellow')}Queen")
  print()
  print()
  print(f"{colorChange('white')}{prev:<12}")
  print(f"{colorChange('green')}{next:^12}")
  print(f"{colorChange('purple')}{pause:>12}")
  

def socialMedia ():
  os.system("clear")
  welcome = "WELCOME TO"
  companyName = "--   ARMBOOK   --"
  slogan = "Definetely not a rip off of"
  slogan2 = "a certain other social"
  slogan3 = "networking site."
  honest = "Honest."
  userName = "Username > "
  userPass = "Password > "
  
  print(f"{colorChange('white')}{welcome:^50}")
  print(f"{colorChange('blue')}{companyName:^50}")
  print()
  print(f"{colorChange('light')}{slogan:^50}")
  print(f"{colorChange('light')}{slogan2:^50}")
  print(f"{colorChange('light')}{slogan3:^50}")
  print("")
  print(f"{colorChange('red')}{honest:^50}")
  print("")
  print("")
  print(f"{colorChange('white')}{userName:^50}")
  print(f"{colorChange('white')}{userPass:^50}")
  


while exit !="y":
  print('\033[?25h', end="")
  classic = "==} CLASSIC UI {=="
  subtitle = "Created using string manipulation"
  print(f"{classic:^55}")
  print(f"{colorChange('light')}{subtitle:^55}\033[0m")
  print("")
  choice = input("Would you like to see the music app or social media \n")
  
  if choice == "music app":
    musicApp()
  elif choice == "social media":
    socialMedia()
  else:
    print("Im not sure I've made that yet")
    print("")
    continue
  
  time.sleep(3)
  exit = input(f"\033[0m exit? (y/n)")
  print("")
  
