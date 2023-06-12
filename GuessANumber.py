import random

number = random.randint(0,100)
attempts = 0 
guess = None

def guessDistance(guess, number):
  difference = abs(guess-number)
  if difference > 50:
    print("You were more than 50 away from my number")
  elif difference > 30: 
    print("You were more than 30 away from my number")
  elif difference > 30: 
    print("You were more than 30 away from my number")
  elif difference > 20:
    print("You were more than 20 away from my number")
  elif difference > 10: 
    print("You were more than 10 away from my number")
  elif difference < 10:
    print("Within 10 of my number")
  else:
    print("")

while guess !=number:
  print("")
  guess = int(input("Guess my number [0-100] "))
  attempts += 1
  
  if guess > number:
    print("Too High!")
  elif guess < number:
    print("Too Low!")

  guessDistance(guess,number)


print()
print("==} YOU WIN {==")
if attempts == 1:
  print("Congratulations! You guessed my number,", number, ",in 1 attempt!")
elif attempts > 1:
  print("Congratulations! You guessed my number,", number, ",in", attempts, "attempts!")
