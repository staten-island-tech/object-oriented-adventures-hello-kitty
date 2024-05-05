from intro import narration
from intro import start
import intro
import middle
import end

class Game:
    def intro(start):
        for i in start:
            if start == "Y":
                print(narration)
            elif start == "N":
                print("Exit terminal.")
            else:
                print("Invalid")

    intro(start)

    def middle():
      for i in range(4):
          question = input("Do you want to go left or right? left or right:")
          if question == "left":
              print("Safe")
          elif question == "right":
              print("Game Over")
              again = input("Do you want to start all over again?: Y or N:")
              if again == "Y":
                  middle()
                  return
              if again == "N":
                  return
              else: 
                  print("Invalid")
          
          while question == "left":
              question = input("Do you want to go left or right? left or right:")
              if question == "right":
                  print("Safe")
              elif question == "left":
                  print("Game Over")
                  again = input("Do you want to start all over again?: Y or N:")
                  if again == "Y":
                    middle()
                    return
                  if again == "N":
                      return
                  else:
                      print("Invalid")
      while True:
          question = input("Are you ready to see what you got?:")
          if question == "Yes":
             print("Yay! You've made it! Take a cork to get a potion bottle!")
             return
          elif question == "No":
             print("Sorry, but I'm afraid this will leave you as incomplete?")
             return
          else:
              print("Invalid")

    middle() 
