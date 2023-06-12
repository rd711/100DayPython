
userTable = int(input("Pick a multiplication table: "))
counter = 0 


for i in range (1,11):
  print(i, "x", userTable)
  rightAnswer = i * userTable
  userAnswer = int(input("Answer > "))

  if rightAnswer == userAnswer:
    print("You're Right")
    print("")
    counter += 1
  else:
    print("The right answer should've been", rightAnswer)
    print("")


if counter == 10:
  print("Wow! A perfect score")
else: 
  print("You scored:", counter, "/ 10")
