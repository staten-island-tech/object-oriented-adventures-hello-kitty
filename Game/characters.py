narration = ("Hello and welcome to the Hello Kitty Potion Game! You are Hello Kitty, and all of your friends have turned evil due to an unknown illness. You will need to compete with your friends in various competitions in order to obtain items for a blueberry potion. At the end of the forest you will find a potion that turns all your friends back to normal.")

def introduction():
 start = (input("Do you wish to start a Sanrio memory game? Y/N: "))
 for i in range(1):
     if start == "Y":
         print(narration)
     elif start == "N":
         print("Exit terminal.")
         exit()
     else:
         print("Invalid")
         exit()
 while start == "Y":
       user_request = input("Do you want to add the main character? Y/N: ")

       for i in range(1):
         if user_request == "Y":
             name = "Hello Kitty"
             skill = "Battling"
             type = "Hero"
             main = "Main character"
             health = 0
             print(name, skill, type, main, health)
         elif user_request == "N":
             exit()
         else:
             print("Invalid")
             exit()
       while user_request == "Y":
         move_on = input("Enter Next:")
         for i in range(1):
             if move_on == "Next":
                 print("Great! Welcome Hello Kitty! You sure are missing your friends.")
                 print("But, wait! Your friends are not what you expected them to be. You might want to know who they are now. Err...")
             else:
                 print("invalid")
                 exit()
  
         while move_on == "Next":
             request = input("Do you want to add enemies?Y/N: ")
             for i in range(1):
                 if request == "Y":
                     name = ["My Melody", "Mimmy", "Pompompurin", "Kuromi", "Pochacco", "Gudetama"]
                     skill = ["Handstand endurance", "Karate", "Bubblegum competition", "Swimming", "Bird  Nest  Making", "Driving Fast"]
                     type = "Enemy"
                     status2= "Infected"
                     health = 0
                     print(name, skill, type, status2, health)
                 elif user_request == "N":
                     exit()
                 else:
                     print("Invalid")
                     exit()
  
             while request == "Y":
                 move_on = input("Enter Next:")
                 for i in range(1):
                     if move_on == "Next":
                         print("Yikes, that's a lot of enemies. But your not alone, a couple of friends are with you. You just won't know who they are.")
                     else:
                         print("Invalid")
                         exit()
      
                 while move_on == "Next":
                     ask_request = input("Do you want to add friends? Y/N: ")
                     for i in range(1):
                         if ask_request == "Y":
                             name = ["Keroppi", "Tuxedo Sam"]
                             skill = ["Cooking", "Making Tie"]
                             type = "Friend"
                             status1 = "Uninfected"
                             health = 0
                             print(name, skill, type, status1, health)
                         elif ask_request == "N":
                             exit()
                         else:
                             print("Invalid")
                             exit()


                     while ask_request == "Y":
                         move_on = input("Enter Next:")
                         for i in range(1):
                             if move_on == "Next":
                                 print("Great. Now that your familiar with what is expected ahead of you.")
                             else:
                                 print("Invalid")
                                 exit()
                  
                         while move_on == "Next":
                             ask = input("Would you like to play the game?:")
                             for i in range(1):
                                 if ask == "Y":
                                     print("Let's begin!")
                                     return
                                 else:
                                     print("Invalid")
                                     exit()

def part1():
  next = input("Welcome! You've entered Level 1! Want to see your first opponent? Y or N:")
  for i in range(1):
      if next == "Y":
          name = "My Melody"
          skill = "Handstand endurance"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across My Melody.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
    move_on = input("My Melody does a handstand for 20 minutes. How long would you do one?: 25 minutes?(L) or 20 minutes(R):")
    for i in range(1):
      if move_on == "L":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 15
          print(name, skill, type, main, health)

          name = "My Melody"
          skill = "Handstand endurance"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 1, with an addition of a solute for yout potion!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

    while move_on == "L":
       level_up = input("Do you want to proceed to the next level? Y or N:")
       for i in range(1):
          if level_up == "Y":
              print("Great! Let's move on!")
              return
          else:
              print("Invalid")
              exit()

def part2():
  next = input("Welcome! You've entered Level 2! Want to see your opponent? Y or N:")
  for i in range(1):
      if next == "Y":
          name = "Mimmy"
          skill = "Swimming"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across Mimmy.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
    move_on = input("Mimmy does karate for 10 minutes. How long would you do one?: 50 minutes?(L) or 20 minutes(R):")
    for i in range(1):
      if move_on == "L":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 30
          print(name, skill, type, main, health)

          name = "Mimmy"
          skill = "Karate"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 2, with an addition of a solvent for your potion!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

    while move_on == "L":
      level_up = input("Do you want to proceed to the next level? Y or N:")
      if level_up == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

def part3():
  next = input("Welcome! You've entered Level 3! Want to see your opponent? Y or N:")
  for i in next:
      if next == "Y":
          name = "Pompompurin"
          skill = "Bubble Gum Competition"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across Pompompurin.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
   move_on = input("Pompompurin chews bubble gum for breaking record of 55 minutes. How long would you do one?: 65 minutes?(R) or 55 minutes(L):")
   for i in range(1):
      if move_on == "R":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 45
          print(name, skill, type, main, health)

          name = "Pompompurin"
          skill = "Bubble Gum Competion"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 3, with an addition of Magic Rocks!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

   while move_on == "R":
      level_up = input("Do you want to proceed to the next level? Y or N:")
      if level_up == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

def part4():
  next = input("Welcome! You've entered Level 4! Oh look, its your a friend. Want to see who it is? Y or N:")
  for i in next:
      if next == "Y":
          name = "Keroppi"
          skill = "Cooking"
          type = "Friend"
          status1= "Uninfected"
          health = 0
          print(name, skill, type, status1, health)
          print("You've come across Keroppi.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
   move_on = input("Keroppi is willing to be on your side. Will you accpet her?: Yes(R) or No(L):")
   for i in range(1):
      if move_on == "R":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 60
          print(name, skill, type, main, health)
          print("Keroppi: I am so happy to be back with you. I think we have another friend to find, but I don't know who they may be.")
          print("You have successfully made through Level 4, with an addition of a Magic Map of the forest!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

   while move_on == "R":
      level_up = input("Do you want to proceed to the next level? Y or N:")
      if level_up == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

def part5():
  next = input("Welcome! You've entered Level 5! Want to see your opponent? Y or N:")
  for i in next:
      if next == "Y":
          name = "Kuromi"
          skill = "Swimming"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across Kuromi.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
   move_on = input("Kuromi swims to the other end of a river in 35 minutes. How long would you do one?: 30 minutes?(R) or 40 minutes(L):")
   for i in range(1):
      if move_on == "R":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 75
          print(name, skill, type, main, health)

          name = "Kuromi"
          skill = "Swimming"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 5, with an addition of a Magic Bag!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

   while move_on == "R":
      level_up = input("Do you want to proceed to the next level? Y or N:")
      if level_up == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

def part6():
  next = input("Welcome! You've entered Level 6! Want to see your opponent? Y or N:")
  for i in next:
      if next == "Y":
          name = "Pochacco"
          skill = "Bird Nest Making"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across Pochacco.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
   move_on = input("Pochacco makes a bird nest in 25 minutes. How long would you do one?: 20 minutes?(L) or 30 minutes(R):")
   for i in range(1):
      if move_on == "L":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 90
          print(name, skill, type, main, health)

          name = "Pochacco"
          skill = "Bird Nest Making"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 6, with an addition of a bottle for your potion!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

   while move_on == "L":
      level_up = input("Do you want to proceed to the next level? Y or N:")
      if level_up == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

def part7():
  next = input("Welcome! You've entered Level 7! Want to see your opponent? Y or N:")
  for i in next:
      if next == "Y":
          name = "Gudetama"
          skill = "Driving Fast"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across Gudetama.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
   move_on = input("Gudetama drives 1 mile in 21 minutes. How long would you do one?: 16 minutes?(L) or 19 minutes(R):")
   for i in range(1):
      if move_on == "L":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 105
          print(name, skill, type, main, health)

          name = "Gudetama"
          skill = "Driving Fast"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 7, with an addtion of a Recipe Book!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

   while move_on == "L":
      level_up = input("Do you want to proceed to the next level? Y or N:")
      if level_up == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

def part8():
  next = input("Welcome! You've entered Level 8! Oh look, its your a friend. Want to see who it is? Y or N:")
  for i in next:
      if next == "Y":
          name = "Tuxedo Sam"
          skill = "Making Tie"
          type = "Friend"
          status1= "Uninfected"
          health = 0
          print(name, skill, type, status1, health)
          print("You've come across Tuxedo Sam.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
   move_on = input("Tuxedo Sam is willing to be on your side. Will you accpet him?: Yes(L) or No(R):")
   for i in range(1):
      if move_on == "L":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 120
          print(name, skill, type, main, health)
          print("Tuxedo Sam : I am so happy to be back with you. I believe we only have one more enemy to come across. Let's defeat them!")
          print("You have successfully made through Level 8, with an addtion of Fairy Dust!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              introduction()
          else:
              print("Good Bye!")
              exit()

   while move_on == "L":
      move = input("Great Job! You have collected all the neccesary items for your potion. Do you want to start making the potion?:")
      if move == "Y":
          print("Great! Let's move on!")
          return
      else:
          print("Invalid")
          exit()

narrator = ("You have obtained all necessary materials to save your friends.")
ending = ("You poured the solution, solute, and fairy dust into the magic bottle for the potion. After you mixed the solution with a branch, put the cork on top and shook it, then you  layed out the magic map and held it in place with magic rocks. Finally, the magic potion was poured on to the magic map and all of your friends were cured from the illness.")
congrats = ("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")

def conclusion():
    question = input("Do you want to see what had happened? Y or N:")
    for i in question:
        if question == "Y":
            print(narrator)
            return
        elif question == "N":
            print("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")
        else:
            print("Invalid")
conclusion()

def restart():
    game_question = input("Do you want to play again?: Y or N:")
    for i in game_question:
        if game_question == "Y":
            introduction()
            part1()
            part2()
            part3()
            part4()
            part5()
            part6()
            part7()
            part8()
            conclusion()
            exit()
        elif game_question == "N":
            print("Hope you had a great time. Good bye!")
        else:
            print("Invalid")
            exit()