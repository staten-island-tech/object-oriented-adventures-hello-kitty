from intro import start
import intro 

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
            print("Total Health: 120 gems")
            return
         elif question == "No":
            print("Sorry, but I'm afraid this will leave you as incomplete.")
            return
         else:
             print("Invalid")
             exit()
  middle()
  exit()

middle() 

