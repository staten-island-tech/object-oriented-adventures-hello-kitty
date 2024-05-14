<<<<<<< HEAD
import intro


def middle():
        question = input("Do you want to go left or right?:")
        if question == "left":
            print("Safe, with an addition of a potion solution")
            print("Health: +15 gems")
        elif question == "right":
            print("Game Over")
            print("Health: 0 gems")
            again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
            if again == "Yes":
                  middle()
                  return
            if again == "No":
                  return
            else:
                  print("Invalid")
        else:
            print("Invalid")
            exit()
      
        while question == "left":
            question = input("Do you want to go left or right?:")
            if question == "right":
                print("Safe, with an addition of a potion solute")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()


        while question == "right":
            question = input("Do you want to go left or right?:")
            if question == "left":
                print("Safe, with an addition of Fairy Dust")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()


        while question == "left":
            question = input("Do you want to go left or right?:")
            if question == "right":
                print("Safe, with an addition of a Magic Mixer")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()


        while question == "right":
            question = input("Do you want to go left or right?:")
            if question == "left":
                print("Safe, with an addition of a Magic bottle")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()
       
        while question == "left":
            question = input("Do you want to go left or right?:")
            if question == "right":
                print("Safe, with an addition of a Magic Map")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()


        while question == "right":
            question = input("Do you want to go left or right?:")
            if question == "left":
                print("Safe, with an addition of a Magic rocks")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()
       
        while question == "left":
            question = input("Do you want to go left or right?:")
            if question == "right":
                print("Safe, with an addition of a cork")
                print("Health: +15 gems")
            elif question == "left":
                print("Game Over")
                print("Health: 0 gems")
                again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                if again == "Yes":
                  middle()
                  return
                if again == "No":
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
                exit()


        while True:
           question = input("Are you ready to see what you got?: Yes or No?:")
           if question == "Yes":
               print("Yay! You've made it! You have collected all the necessary things for your potion.")
               print("Total Health: 120 gems")
               exit()
           elif question == "No":
               print("Sorry, but I'm afraid this will leave you as incomplete.")
               exit()
           else:
               print("Invalid")
               exit()
middle()
=======
<<<<<<< HEAD
import intro

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
              intro
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
part1()

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
              intro
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
part2()

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
              intro
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
part3()

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
              intro
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
part4()

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
              intro
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
part5()

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
              intro
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
part6()

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
              intro
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
part7()

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
              intro
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
part8()
=======
from intro import start
import intro 

while start == "Y": 
  def middle():
         question = input("Do you want to go left or right?:")
         if question == "left":
             print("Safe, with an addition of a potion solution")
             print("Health: +15 gems")
         elif question == "right":
             print("Game Over")
             print("Health: 0 gems")
             again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
             if again == "Yes":
                   middle()
                   return
             if again == "No":
                   return
             else:
                   print("Invalid")
         else:
             print("Invalid")
             exit()
        
         while question == "left":
             question = input("Do you want to go left or right?:")
             if question == "right":
                 print("Safe, with an addition of a potion solute")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()

         while question == "right":
             question = input("Do you want to go left or right?:")
             if question == "left":
                 print("Safe, with an addition of Fairy Dust")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()

         while question == "left":
             question = input("Do you want to go left or right?:")
             if question == "right":
                 print("Safe, with an addition of a Magic Mixer")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()

         while question == "right":
             question = input("Do you want to go left or right?:")
             if question == "left":
                 print("Safe, with an addition of a Magic bottle")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()
         
         while question == "left":
             question = input("Do you want to go left or right?:")
             if question == "right":
                 print("Safe, with an addition of a Magic Map")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()

         while question == "right":
             question = input("Do you want to go left or right?:")
             if question == "left":
                 print("Safe, with an addition of a Magic rocks")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()
         
         while question == "left":
             question = input("Do you want to go left or right?:")
             if question == "right":
                 print("Safe, with an addition of a cork")
                 print("Health: +15 gems")
             elif question == "left":
                 print("Game Over")
                 print("Health: 0 gems")
                 again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                 if again == "Yes":
                   middle()
                   return
                 if again == "No":
                     return
                 else:
                     print("Invalid")
             else:
                 print("Invalid")
                 exit()

         while True:
            question = input("Are you ready to see what you got?: Yes or No?:")
            if question == "Yes":
                print("Yay! You've made it! You have collected all the necessary things for your potion.")
                print("Total Health: 120 gems")
                exit()
            elif question == "No":
                print("Sorry, but I'm afraid this will leave you as incomplete.")
                exit()
            else:
                print("Invalid")
                exit()
  middle()
>>>>>>> Hongzheng-Wu
>>>>>>> d5668d79d5481ec7628e16f39f09cfed4d5ad4eb
