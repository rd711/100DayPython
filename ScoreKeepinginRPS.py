# from getpass import getpass as input
# known error: doesn't filter non R, P, S inputs

print("=={Rock Paper Scissors }==")


player1score = 0
player2score = 0


while True: 
  if player1score > 0 or player2score > 0:
    print("")
    print("CURRENT SCORE:")
    print("Player 1:", player1score)
    print("Player 2:", player2score)
    print("")
    
  print("Select R, P or S")
  player1Choice = input("Player 1 > ")
  player2Choice = input("Player 2 > ")
  print()
  
  if player1Choice == player2Choice:
    print ("It's a tie!")
  elif player1Choice == "R":
    if player2Choice == "P":
      print("Paper beats rock! Player 2 wins!")
      player2score += 1
    elif player2Choice == "S":
      print("Rock beats scissors! Player 1 wins!")
      player1score += 1
  elif player1Choice == "P":
    if player2Choice == "S":
      print("Scissors beats paper! Player 2 wins!")
      player2score += 1
    elif player2Choice == "R":
      print("Paper beats rock! Player 1 wins!")
      player1score += 1
  elif player1Choice == "S":
    if player2Choice == "R":
      print("Rock beats scissors! Player 2 wins!")
      player2score += 1
    elif player2Choice == "P":
      print("Scissors beats paper! Player 1 wins!")
      player1score += 1
  if player1score == 3 or player2score == 3:
    if player1score > player2score:
      print("Player1 Wins!")
      break
    if player2score > player1score:
      print("Player2 Wins Overall!")
      break
  else:
    continue
    
  
