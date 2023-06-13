import random

play = "yes"

def rollDice(sides):
  rollPsu = random.randint(1,sides)
  return rollPsu
  
def charHealth():
  diceSix = rollDice(6)
  diceEight = rollDice(8)
  health = diceSix * diceEight
  return health
  



while play != "no":
  name = input("Enter a name for your charachter ")
  health = str(charHealth())
  print(name,":", health, "hp")
  play = input("Continue? ")
  print('')
