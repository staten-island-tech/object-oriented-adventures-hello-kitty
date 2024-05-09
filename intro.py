<<<<<<< Updated upstream
narrator = ("You are Hello Kitty. All of your friends have turned evil due to an unknown illness! You need to compete with your friends in competitions inorder to obtain items for the potion.At the end of the forest you will find a potion that turns all your friends back to normal.")
start = (input("Do you wish to start a Sanrio memory game? Y/N: "))
def intro(start):
    for i in start:
        if start == "Y":
            print(narrator)
        elif start == "N":
            print("Exit Game. We hope to see you again!")
        else:
            print("Invalid")
intro(start)
=======
from enemy import create_main
narration = ("You are Hello Kitty. All of your friends have turned evil due to an unknown illness! You need to memorize the paths that your friends are not on, in order to make it to the end of the forest.At the end of the forest you will find a potion that turns all your friends back to normal.")
add_heros = 'Y'
start = (input("Do you wish to start a Sanrio memory game? Y/N: "))

def intro(start):
    for i in start:
        if start == "Y":
            print(narration)
        elif start == "N":
            print("Exit terminal.")
        else:
            print("Invalid")

    while add_heros == "Y":
     user_request = input("Do you want to add the main character? Y/N: ")
     if user_request == "Y":
      name = "Hello Kitty"
      skill = "Battling"
      type = "Hero"
      main = "Main character"
      create_main(name, skill, type, main)
     elif user_request == "N":
       break
     else:
       print("Invalid")
>>>>>>> Stashed changes
