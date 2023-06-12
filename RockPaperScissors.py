from getpass import getpass as input

print("=={Rock Paper Scissors }==")
print()
print("Select R, P or S")

player1Choice = input("Player 1 > ")
print()
player2Choice = input("Player 2 > ")
print()

if player1Choice == player2Choice:
  print ("It's a tie!")
elif player1Choice == "R":
  if player2Choice == "P":
    print("Paper beats rock! Player 2 wins!")
  elif player2Choice == "S":
    print("Rock beats scissors! Player 1 wins!")
elif player1Choice == "P":
  if player2Choice == "S":
    print("Scissors beats paper! Player 2 wins!")
  elif player2Choice == "R":
    print("Paper beats rock! Player 1 wins!")
elif player1Choice == "S":
  if player2Choice == "R":
    print("Rock beats scissors! Player 2 wins!")
  elif player2Choice == "P":
    print("Scissors beats paper! Player 1 wins!")
else:
  print('Check your inputs')
