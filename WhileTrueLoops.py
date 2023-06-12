print("Fill in the blanks!")
print("Never going to ______ you up.")
print("")

counter = 0 
while True:
  userBlank = input("Type in the blank lyrics: ")
  if userBlank == "give" or userBlank == "Give":
    if counter == "0":
      print ("Wow, you got it your first try")
    elif counter > 0: 
      print("Wow it only took you", counter, "attempts")
    break
  else:
    counter += 1
    print("Nope, try again.")
    print("")
    
