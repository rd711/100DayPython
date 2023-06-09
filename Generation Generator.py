print("=={ What generation are you part of? }==")
print("")

userDOB = int(input("What year were you born? "))
if userDOB <= 1907:
  print("I'm gonna need some proof..")
elif userDOB < 1923 and userDOB >= 1908: 
  print("Wow! You're over 100. Got any tips?")
elif userDOB == 1923: 
  print("Wow! You're 100!! Got any tips?")
elif userDOB == 1924:
  print("Wow! You're almost 100. Got any tips?")
elif userDOB >= 1925 and userDOB <= 1946:
  print("You're part of the Traditionalists Generation")
elif userDOB >= 1947 and userDOB <= 1964:
  print("You're part of the Baby Boomers Generation")
elif userDOB >= 1965 and userDOB <= 1981:
  print("You're part of Generation X Generation")
elif userDOB >= 1982 and userDOB <= 1995:
  print("You're part of the Millenials Generation")
elif userDOB >= 1996 and userDOB <= 2015:
  print("You're part of Generation Z")
else :
  print("Who let the baby on the computer?.. ")