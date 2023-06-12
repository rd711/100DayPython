totalBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tipBill = float(input("What % would you like to tip?: ")) /100
userBill = round(totalBill / numberOfPeople * (1  + tipBill),2)
print ("You all owe", userBill)
