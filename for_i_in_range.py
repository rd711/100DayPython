
print("==}APR Calc }==")
userAPR = int(input("APR {%} > ")) 
loan = int(input("Loan size > "))
duration = int(input("Duration > "))
apr = userAPR / 100

print("")
print("==} Interest {==")
for i in range (duration):
  loan += loan*apr
  print("Year", i + 1, '~', round(loan,2))
