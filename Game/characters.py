import characters2
import uuid
import json
import os

# Open the JSON file of pokemon data
narration = ("Hello and welcome to the Hello Kitty Potion Game! You are Hello Kitty, and all of your friends have turned evil due to an unknown illness. You will need to compete with your friends in various competitions in order to obtain items for a blueberry potion. At the end of the forest you will find a potion that turns all your friends back to normal.")
narrator = ("You have obtained all necessary materials to save your friends.")
ending = ("You poured the solution, solute, and fairy dust into the magic bottle for the potion. After you mixed the solution with a branch, put the cork on top and shook it, then you  layed out the magic map and held it in place with magic rocks. Finally, the magic potion was poured on to the magic map and all of your friends were cured from the illness.")
congrats = ("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")

class characters:
  def __init__(self, name, skill, type, health):
      self.name = name
      self.skill = skill    
      self.type = type
      self.health = health
class Main_characters(characters):
  def __init__(self, name, skill, type, main, health):
      super().__init__(name,skill, type, health)
      self.main= main
  def __str__(self):
      return f"{self.name},{self.skill},{self.type}, {self.main}, {self.health}"
class friends_lst(characters):
  def __init__(self, name, skill, type, status1, health):
      super().__init__(name,skill, type, health)
      self.status1 = status1
  def __str__(self):
      return f"{self.name}, {self.skill},{self.type}, {self.status1}, {self.health}"
class enemies_lst(characters):
  def __init__(self, name, skill, type, status2, health):
      super().__init__(name,skill, type, health)
      self.status2 = status2
  def __str__(self):
          return f"{self.name}, {self.skill},{self.type}, {self.status2}, {self.health}"

user_request ="Y"

def check_stat(stat): #This checks the status to see if the user put Y or not.
 if stat.upper == "Y":
     return True
 else:
     return False

def create_main(name, skill, type, health, main):
    MAIN = {
        "name" : name,
        "skill" : skill,
        "type" : type,
        "health" : health,
        "main" : main
    }
    
    return MAIN

def create_enemies(name, skill, type, health, status1):
    enemies = {
        "name" : name,
        "skill" : skill,
        "type" : type,
        "health" : health,
        "status1" : status1
    }
    
    return enemies

def create_friends(name, skill, type, health, status2):
    friends = {
        "name" : name,
        "skill" : skill,
        "type" : type,
        "health" : health,
        "status2" : status2
    }
    
    return friends

data = []

def check_stat(stat): #This checks the status to see if the user put Y or not.
 if stat.lower == "y":
     return True
 else:
     return False
 
class Game():
  def beginning():
    ask = input("Do you want to play a Sanrio memory game? Y/N:")
    if ask.upper() == "Y":
        start = print("Hello and welcome to the Hello Kitty Potion Game! You are Hello Kitty, and all of your friends have turned evil due to an unknown illness. You will need to compete with your friends in various competitions in order to obtain items for a blueberry potion. At the end of the forest you will find a potion that turns all your friends back to normal.")
    elif ask.upper() == "N":
        print("Exit terminal.")
        exit()
    else:
        print("Invalid")
        exit()
  beginning()

  def middle():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 1! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "My Melody"
        skill = "Handstand endurance"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        create_enemies(name, skill, type, status1, health)
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("My Melody does a handstand for 20 minutes. How long would you do one?: 25 minutes?(L) or 20 minutes(R):")
        if move == "L":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 15
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 1, with an addition of a solute for your potion!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle()

  def middle2():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 2! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Mimmy"
        skill = "Swimming"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        create_enemies(name, skill, type, status1, health)
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Mimmy does karate for 10 minutes. How long would you do one?: 50 minutes?(L) or 20 minutes(R):")
        if move == "L":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 30
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 2, with an addition of a solvent for your potion!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()  
  middle2()

  def middle3():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 3! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Pompompurin"
        skill = "Bubble Gum Competition"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        create_enemies(name, skill, type, status1, health)
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Pompompurin chews bubble gum for breaking record of 55 minutes. How long would you do one?: 65 minutes(R) or 55 minutes(L):")
        if move == "R":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 45
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 3, with an addition of Magic Rocks!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle3()

  def middle4():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 4! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Keroppi"
        skill = "Cooking"
        type = "Friend"
        status2 = "Uninfected"
        health = 0
        create_friends(name, skill, type, status2, health)
        new_info = create_friends(name, skill, type, status2, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Keroppi is willing to be on your side. Will you accpet her?: Yes(R) or No(L):")
        if move == "R":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 60
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("Keroppi: I am so happy to be back with you. I think we have another friend to find, but I don't know who they may be.")
            print("You have successfully made through Level 4, with an addition of a Magic Map of the forest!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle4()

  def middle5():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 5! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Kuromi"
        skill = "Swimming"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        create_enemies(name, skill, type, status1, health)
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Kuromi swims to the other end of a river in 35 minutes. How long would you do one?: 30 minutes?(R) or 40 minutes(L):")
        if move == "R":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 75
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 5, with an addition of a Magic Bag!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle5()  

  def middle6():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 6! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Pochacco"
        skill = "Bird Nest Making"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        create_enemies(name, skill, type, status1, health)
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Pochacco makes a bird nest in 25 minutes. How long would you do one?: 20 minutes?(L) or 30 minutes(R):")
        if move == "L":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 90
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 6, with an addition of a bottle for your potion!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle6()  

  def middle7():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 7! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Gudetama"
        skill = "Driving Fast"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        create_enemies(name, skill, type, status1, health)
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Gudetama drives 1 mile in 21 minutes. How long would you do one?: 16 minutes?(L) or 19 minutes(R):")
        if move == "L":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 105
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 7, with an addition of a Recipe Book!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle7()

  def middle8():
    add_more_characteristics = "Y"
    still_continue = input("Welcome! You've entered Level 8! Want to see your opponent? Y or N:").upper()
    add_more_characteristics == still_continue
    if add_more_characteristics == "Y":
        still_continue
        name = "Tuxedo Sam"
        skill = "Making Tie"
        type = "Friend"
        status2 = "Uninfected"
        health = 0
        create_friends(name, skill, type, status2, health)
        new_info = create_friends(name, skill, type, status2, health)
        data.append(new_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "Y":
        move = input("Tuxedo Sam is willing to be on your side. Will you accpet him?: Yes(L) or No(R):")
        if move == "L":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 120
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            print("You have successfully made through Level 8, with an addition of Fairy Dust!")
        else:
            print("Invalid")
            exit()

    characters2.go_on()
  middle8() 

  def end():
    ask = input("Do you want to see what had happened? Y or N:")
    if ask.upper() == "Y":
        result = print(narrator)
    elif ask.upper() == "N":
        print("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")
        exit()
    else:
        print("Invalid")
        exit()
   
  end()

new_file = "update.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.rename(new_file, "update.json")

data.append(data)