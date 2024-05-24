import uuid
class characters:
    def __init__(self, name, skill, type):
        self.name = name
        self.skill = skill      
        self.type = type
   
class Main_characters(characters):
    def __init__(self, name, skill, type, main):
        super().__init__(name,skill, type)
        self.main= main
    def __str__(self):
        return f"{self.name},{self.skill},{self.type}, {self.main}"
class friends_lst(characters):
    def __init__(self, name, skill, type, status1):
        super().__init__(name,skill, type)
        self.status1 = status1
    def __str__(self):
        return f"{self.name}, {self.skill},{self.type}, {self.status1}"
class enemies_lst(characters):
    def __init__(self, name, skill, type, status2):
        super().__init__(name,skill, type)
        self.status2 = status2
    def __str__(self):
            return f"{self.name}, {self.skill},{self.type}, {self.status2}"
main_characters= []
all_friends= []
all_enemies= []


def create_main(name, skill, type, main):
    new_main = Main_characters(name, skill, type, main)
    main_characters.append(new_main)
    for characters in main_characters:
        print(characters)


def create_friends(name, skill,type, status1):
    new_friends = friends_lst(name, skill, type, status1)
    all_friends.append(new_friends)
    for friends in all_friends:
        print(friends)


def create_enemies5(name, skill, type, status2):
    new_enemies = enemies_lst(name, skill, type, status2)
    all_enemies.append(new_enemies)
    for enemies in all_enemies:
        print(enemies)


add_heros ="Y"
def check_stat(stat): #This checks the status to see if the user put Y or not.
    if stat.upper == "Y":
        return True
    else:
        return False
   
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




add_enemies = "Y"
def check_stat(stat): #This checks the status to see if the user put Y or not.
    if stat.upper == "Y":
        return True
    else:
        return False
   
while add_enemies =="Y":
    request = input("Do you want to add enemies?Y/N: ")
    if request == "Y":
      name = "My Melody"
      skill = "Handstand endurance"
      type = "Enemy"
      status2= "Infected"
      create_enemies5(name, skill, type, status2)
      name = "Mimmy"
      skill = "Karate"
      type = "Enemy"
      status2= "Infected"
      create_enemies5(name, skill, type, status2)
      name = "Pompompurin"
      skill = "Bubblegum competition"
      type = "Enemy"
      status2= "Infected"
      create_enemies5(name, skill, type, status2)
      name ="Kuromi"
      skill = "Swimming"
      type = "Enemy"
      status2 = "Infected"
      create_enemies5(name, skill, type, status2)
      name ="Pochacco"
      skill = "bird nest making"
      type = "Enemy"
      status2 = "Infected"
      create_enemies5(name, skill, type, status2)
      name ="Gudetama"
      skill = "driving fast"
      type = "Enemy"
      status2 = "Infected"
      create_enemies5(name, skill, type, status2)
    elif user_request == "N":
       break
    else:
       print("invalid")




add_friends = "Y"
def check_stat(stat): #This checks the status to see if the user put Y or not.
    if stat.upper == "Y":
        return True
    else:
        return False
while add_friends =="Y":
    ask_request = input("Do you want to add friends? Y/N: ")
    if ask_request == "Y":
        name = "Keroppi"
        skill = "Cooking"
        type = "Friend"
        status1 = "Uninfected"
        create_friends(name, skill, type, status1)
        name = "Tuxedo Sam"
        skill = "making tie"
        type = "friend"
        create_friends(name, skill, type, status1)
    elif ask_request == "N":
        break
    else:
        print("Invalid")