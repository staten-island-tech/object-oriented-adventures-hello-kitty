<<<<<<< HEAD
#Hongzheng
=======
import json
import os
# Open the JSON file of pokemon data
tests = open("sanrio_characters.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
sanrio_characters = json.load(tests)

>>>>>>> Afsheen
import uuid
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
main_characters= []
all_friends= []
all_enemies= []


def create_main(name, skill, type, main, health):
 new_main = Main_characters(name, skill, type, main, health)
 main_characters.append(new_main)
 for characters in main_characters:
     print(characters)


def create_friends(name, skill,type, status1, health):
 new_friends = friends_lst(name, skill, type, status1, health)
 all_friends.append(new_friends)
 for friends in all_friends:
     print(friends)


def create_enemies5(name, skill, type, status2, health):
 new_enemies = enemies_lst(name, skill, type, status2, health)
 all_enemies.append(new_enemies)
 for enemies in all_enemies:
     print(enemies)


user_request ="Y"


def check_stat(stat): #This checks the status to see if the user put Y or not.
 if stat.upper == "Y":
     return True
 else:
     return False
 
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(sanrio_characters)

    f.write(json_string)

os.remove("sanrio_characters.json")
os.rename(new_file, "sanrio_characters.json")

sanrio_characters.append(sanrio_characters)