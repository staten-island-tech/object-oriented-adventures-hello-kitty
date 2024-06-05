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
new_info = create_enemies
new_file = "update.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

data.append(data)


class function:
    def __init__(self, ask):
        self.ask = ask

class introduction(function):
    def __init__(self, ask, start):
        super().__init__(ask)
        self.start = start
    def __str__(self):
        return f"{self.start}, {self.ask}"
   
class parts(function):
    def __init__(self, ask, move):
        super().__init__(ask)
        self.move = move
    def __str__(self):
        return f"{self.ask}, {self.move}"


class conclusion(function):
    def __init__(self, ask, result):
        super().__init__(ask)
        self.result = result
    def __str__(self):
        return f"{self.ask}, {self.result}"

       
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
        pass
    elif ask.upper() == "N":
        print("Exit terminal.")
        exit()
    else:
        print("Invalid")
        exit()
  beginning()

  def middle():
    ask = input("Welcome! You've entered Level 1! Want to see your first opponent? Y or N:")
    if ask.upper() == "Y":
        name = "My Melody"
        skill = "Handstand endurance"
        type = "Enemy"
        status1 = "Infected"
        health = 0
        new_info = create_enemies(name, skill, type, status1, health)
        data.append(new_info)
        print("You've come across My Melody.")
    else:
        print("Invalid")
        exit()


    move = input("My Melody does a handstand for 20 minutes. How long would you do one?: 25 minutes?(L) or 20 minutes(R):")
    if move == "L":
        create_main("Hello Kitty", "Battling", "Main Character", "Hero", 15)
        print("You have successfully made through Level 1, with an addition of a solute for your potion!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()


    ask = input("Welcome! You've entered Level 2! Want to see your opponent? Y or N:")
    if ask.upper() == "Y":
      classes.create_enemies5("Mimmy", "Swimming", "Enemy", "Infected", 0)
      print("You've come across Mimmy.")
    else:
      print("Invalid")
      exit()
     
    move = input("Mimmy does karate for 10 minutes. How long would you do one?: 50 minutes?(L) or 20 minutes(R):")
    if move == "L":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 30)
        print("You have successfully made through Level 2, with an addition of a solvent for your potion!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()
     
    ask = input("Welcome! You've entered Level 3! Want to see your opponent? Y or N:")
    if ask.upper() == "Y":
        classes.create_enemies5("Pompompurin", "Bubble Gum Competition", "Enemy", "Infected", 0)
        print("You've come across Pompompurin.")
    else:
        print("Invalid")
        exit()


    move = input("Pompompurin chews bubble gum for breaking record of 55 minutes. How long would you do one?: 65 minutes?(R) or 55 minutes(L):")
    if move == "R":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 45)
        print("You have successfully made through Level 3, with an addition of Magic Rocks!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()


    ask = input("Welcome! You've entered Level 4! Oh look, its your a friend. Want to see who it is? Y or N:")
    if ask.upper() == "Y":
        classes.create_friends("Keroppi","Cooking", "Friend", "Uninfected", 0)
        print("You've come across Keroppi.")
    else:
        print("Invalid")
        exit()
 
    move = input("Keroppi is willing to be on your side. Will you accpet her?: Yes(R) or No(L):")
    if move == "R":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 60)
        print("Keroppi: I am so happy to be back with you. I think we have another friend to find, but I don't know who they may be.")
        print("You have successfully made through Level 4, with an addition of a Magic Map of the forest!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()


    ask = input("Welcome! You've entered Level 5! Want to see your opponent? Y or N:")
    if ask.upper() == "Y":
        classes.create_enemies5("Kuromi", "Swimming", "Enemy", "Infected", 0)
        print("You've come across Kuromi.")
    else:
        print("Invalid")
        exit()


    move = input("Kuromi swims to the other end of a river in 35 minutes. How long would you do one?: 30 minutes?(R) or 40 minutes(L):")
    if move == "R":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 75)
        print("You have successfully made through Level 5, with an addition of a Magic Bag!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()


    ask = input("Welcome! You've entered Level 6! Want to see your opponent? Y or N:")
    if ask.upper() == "Y":
        classes.create_enemies5("Pochacco", "Bird Nest Making", "Enemy", "Infected", 0)
        print("You've come across Pochacco.")
    else:
        print("Invalid")
        exit()


    move = input("Pochacco makes a bird nest in 25 minutes. How long would you do one?: 20 minutes?(L) or 30 minutes(R):")
    if move == "L":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 90)
        print("You have successfully made through Level 6, with an addition of a bottle for your potion!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()


    ask = input("Welcome! You've entered Level 7! Want to see your opponent? Y or N:")
    if ask.upper() == "Y":
        classes.create_enemies5("Gudetama", "Driving Fast", "Enemy", "Infected", 0)
        print("You've come across Gudetama.")
    else:
        print("Invalid")
        exit()


    move = input("Gudetama drives 1 mile in 21 minutes. How long would you do one?: 16 minutes?(L) or 19 minutes(R):")
    if move == "L":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 105)
        print("You have successfully made through Level 7, with an addition of a Recipe Book!")
    else:
        print("Invalid")
        exit()


    characters2.go_on()


    ask = input("Welcome! You've entered Level 8! Oh look, its your a friend. Want to see who it is? Y or N:")
    if ask.upper() == "Y":
        classes.create_friends("Tuxedo Sam", "Making Tie", "Friend", "Uninfected", 0)
        print("You've come across Tuxedo Sam.")
    else:
        print("Invalid")
        exit()


    move = input("Tuxedo Sam is willing to be on your side. Will you accpet him?: Yes(L) or No(R):")
    if move == "L":
        classes.create_main("Hello Kitty", "Battling", "Main Character", "Hero", 120)
        print("Tuxedo Sam : I am so happy to be back with you. I believe we only have one more enemy to come across. Let's defeat them!")
        print("You have successfully made through Level 8, with an addition of Fairy Dust!")
    else:
        print("Invalid")
        exit()


    move = input("Great Job! You have collected all the neccesary items for your potion. Do you want to start making the potion?: Y or N:")
    if move.upper() == "Y":
        print("Great! Let's move on!")
    else:
        print("Invalid")
        exit()
   
  middle()


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
