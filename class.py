<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 89d7167d69546338744268f360fa457457d363be
narration = ("You are Hello Kitty. All of your friends have turned evil due to an unknown illness! You need to memorize the paths that your friends are not on, in order to make it to the end of the forest.At the end of the forest you will find a potion that turns all your friends back to normal.")
start = (input("Do you wish to start a Sanrio memory game? Y/N: "))

class Game:
    def intro(start): 
        for i in start:
            if start == "Y":
                print(narrator)
<<<<<<< HEAD
=======
=======
from intro import narration
from intro import start
import intro
import middle

class Game:
    def intro(start):   
        for i in start:
            if start == "Y":
                print(narration)
>>>>>>> Afsheen
>>>>>>> 89d7167d69546338744268f360fa457457d363be
            elif start == "N":
                print("Exit terminal.")
            else:
                print("Invalid")
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 89d7167d69546338744268f360fa457457d363be
                exit()
    intro(start)

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
<<<<<<< HEAD
=======
=======

    intro(start)

    while start == "Y": 
        def middle():         
          for i in range(4):
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
                        print("Safe, with an addition of a potion solution")
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
                print("Yay! You've made it! You have 8 potion solutions, and a cork for your potion bottle.")
>>>>>>> Afsheen
>>>>>>> 89d7167d69546338744268f360fa457457d363be
                print("Total Health: 120 gems")
                return
            elif question == "No":
                print("Sorry, but I'm afraid this will leave you as incomplete.")
                return
            else:
                print("Invalid")
                exit()
<<<<<<< HEAD
    middle()
    exit()
=======
<<<<<<< HEAD
    middle()
    exit()
=======
        middle()
        exit()
>>>>>>> Afsheen
>>>>>>> 89d7167d69546338744268f360fa457457d363be
