## Intro
print("==={ ABOUT YOU }===")
userName = input("What is your name? ")
print("Nice to meet you, ", userName)
print("")
userGoals = input("What are some of your goals? ")
print("I'm glad to hear you have a clear goal of", userGoals)
print("")
dayWeek = input("Remind me, what day of the week is it? ")

## Sub optimal day filter
## Dont need to ask for day twice
if dayWeek == "Monday" or dayWeek == "monday" or dayWeek == "Tuesday" or dayWeek == "tuesday" or dayWeek == "Wednesday" or dayWeek == "wednesday" or dayWeek == "Thursday" or dayWeek == "thursday" or dayWeek == "Friday" or dayWeek == "friday" or dayWeek == "Saturday" or dayWeek == "saturday" or dayWeek == "Sunday" or dayWeek == "sunday":
    print("Of course it is.. How could I forget?..")
    print("")
    userEmote = input("How are you feeling today?")
    
    if userEmote == "Happy" or userEmote == "happy" or userEmote == "motivated" or userEmote == "Motivated":
      print("I'm very glad you're feeling ", userEmote "I hope these affirmations can help boost that feeling of", userEmote, "even more..")
      print("")
      print("==={ YOUR AFFIRMATION }===")
      if dayWeek == "Monday" or dayWeek == "monday":
        print("Remember, ",  userName "Progress is to make small steps towards big goals take one step toward that goal of", userGoals "today")
      elif dayWeek == "Tuesday" or dayWeek == "tuesday":
        print("Take today to remind yourself, " , userName "that you are motivated, positive, confident in your path towards that goal of", userGoals)
      elif dayWeek == "Wednesday" or dayWeek == "wednesday":
        print(userName, "You are full of vitality. Your confidence, positive attitude, and self-belief are my biggest assets to take me a step closer to that goal of", userGoals)
      elif dayWeek == "Thursday" or dayWeek == "thursday":
        print("Each and every day, you," userName, ",are getting closer to achieving your goal of", userGoals)
      elif dayWeek == "Friday" or dayWeek == "friday":
        print("As you work towards your goal of", userGoals, "dont forget to be thankful and proud of where you are right now", userName)
      elif dayWeek == "Saturday" or dayWeek == "saturday":
        print("You are getting close to success, I can feel it,",  userName ". That goal of", userGoals "is so close ")
      elif dayWeek == "Sunday" or dayWeek == "sunday":
        print("Remember", userName, "sieze the day before you today everyday of hard work is one day closer to that dream of" , userGoals)
    
    if userEmote == "Sad" or userEmote == "sad" or userEmote == "Low" or userEmote == "Low":
      print("Oh, I'm sorry you're feeling", userEmote, "hopefully some affirmations can lighten your mood..")
      print("")
      print("==={ YOUR PERSONAL DAILY AFFIRMATION }===")
      if dayWeek == "Monday" or dayWeek == "monday":
        print("You sadness and your depression do not define you," userName, "don't let it get in the way of your goal of", userGoals)
      elif dayWeek == "Tuesday" or dayWeek == "tuesday":
        print("You are needed regardless of how worthless you feel", userName. "that goal of ",  userGoals 'needs you..')
      elif dayWeek == "Wednesday" or dayWeek == "wednesday":
        print("You have made it this far, and you won’t stop now", userName. "Keep that goal of" userGoals "clear in your mind and stay steadfast")
      elif dayWeek == "Thursday" or dayWeek == "thursday":
        print("You are resilient in the face of any challenge.", userName, "The fact that you are so determined to achive your goal of", userGoals "proves it so.")
      elif dayWeek == "Friday" or dayWeek == "friday":
        print("You are capable and driven to overcoming this slump", userName. "Take a break and when you come back, I want you to prove everyone wrong and achieve that goal of", userGoals)
      elif dayWeek == "Saturday" or dayWeek == "saturday":
        print(userName, "have faith in your ability. If you are determined enough, you can achieve anything you want, including that goal of " userGoals)
      elif dayWeek == "Sunday" or dayWeek == "sunday":
        print("These feelings will pass," userName 'and when they do, you will achieve all things you could possibly dream of, especially that goal of',  userGoals)
  
    else:
      print("I'm sorry, my vocabulary is quite low.. I'm only new. Please express your emotions as Happy, Motivated, Sad or Low")
else:
    print("That's not a day of the week silly...")
