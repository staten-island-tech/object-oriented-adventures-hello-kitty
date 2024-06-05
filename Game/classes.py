import json
import os
# Open the JSON file of pokemon data
tests = open("sanrio_characters.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
sanrio_characters = json.load(tests)

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


new_characteristics_info = create_main()
new_characteristics_info = create_enemies()
new_characteristics_info = create_friends()
data.append(new_characteristics_info)
    
new_file = "update.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("updated.json")
os.rename(new_file, "update.json")

data.append(data)