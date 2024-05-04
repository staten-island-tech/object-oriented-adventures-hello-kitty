narration = ("You are Hello Kitty. All of your friends have turned evil due to an unknown illness! You need to memorize the paths that your friends are not on, in order to make it to the end of the forest.At the end of the forest you will find a potion that turns all your friends back to normal.")
start = (input("Do you wish to start a Sanrio memory game? Y/N: "))
def intro(start):
    for i in start:
        if start == "Y":
            print(narration)
        elif start == "N":
            print("Exit terminal.")
        else:
            print("Invalid")
intro(start)

right = "<"
question = None
left = ">"

def middle():
      for i in range(4):
          question = input("Do you want to go left or right?")
          if question == "left":
              print("Safe")
          elif question == "right":
              print("Game Over")
              intro(start)
    
          while question == "left":
              question = input("Do you want to go left or right?")
              if question == "right":
                  print("Safe")
              elif question == "left":
                  print("Game Over")
                  intro(start)


      question = input("Are you ready to see what you got?")
      if question == "Yes":
          print("Yay! You've made it! Take a cork to get a potion bottle!")
      elif question == "No":
          print("Sorry, but I'm afraid this will leave you as incomplete?")


middle() 
