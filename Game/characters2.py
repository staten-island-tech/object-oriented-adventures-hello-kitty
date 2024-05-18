from classes import create_main
from classes import create_enemies5
from classes import create_friends

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
             create_main(name, skill, type, main, health)
         elif user_request == "N":
             break
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
                     create_enemies5(name, skill, type, status2, health)
                 elif user_request == "N":
                     break
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
                             create_friends(name, skill, type, status1, health)
                         elif ask_request == "N":
                             break
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
introduction()
