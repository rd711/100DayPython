#Used to test outputs
#percentageRecieved = int(input("Points to test: "))
#testName = "Python"

#User inputs
testName = input("What was the name of your test?: ")
scoreMax = int(input("What was the maximum points you could recieve?: "))
pointsRecieved = int(input("How many points did you score?: "))
percentageRecieved = round((pointsRecieved / scoreMax) * 100, 2)
print("")



#Grading
print("==} RESULTS {==")
if percentageRecieved >= 90 and percentageRecieved <=100:
  print("On your", testName,  "test, you scored", percentageRecieved, "%. Which an A+!")
elif percentageRecieved >= 80 and percentageRecieved <=89:
  print("On your", testName,  "test, you scored", percentageRecieved, "% which an A!")
elif percentageRecieved >= 70 and percentageRecieved <=79:
  print("On your", testName,  "test, you scored", percentageRecieved, "% which a B!")
elif percentageRecieved >= 60 and percentageRecieved <=69:
  print("On your", testName,  "test, you scored", percentageRecieved, "% which a C!")
elif percentageRecieved >= 50 and percentageRecieved <=59:
  print("On your", testName,  "test, you scored", percentageRecieved, "% which a D!")
elif percentageRecieved < 50 and percentageRecieved >=0:
  print("On your", testName,  "test, you scored", percentageRecieved, "% which a fail.!")
else:
  print("Check your inputs again")
