exit = ""
while exit !="yes":
  print()
  userAnimal = input("What animal do you want? ")
  if userAnimal == "Cow" or userAnimal == "cow":
    print("A cow goes moo")
  elif userAnimal == "Lemur" or userAnimal == "lemur":
    print("Ummm...the Lesser Spotter Lemur goes awooga.")
  else:
    print("I'm not sure I know that animal..")
  exit = input("Do you want to exit? (Yes/No)")
