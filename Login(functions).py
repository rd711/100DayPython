def login ():
  while True:
    username = input("Username >")
    password = input("Password >")
    if username == "David" and password == "123":
      print("")
      print("Welcome back, David")
      break
    else:
      print("Swiper no swiping")
      continue
print("==} SECURE LOGIN {==")
login()
