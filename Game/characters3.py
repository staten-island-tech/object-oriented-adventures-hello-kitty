import json
import os
# Open the JSON file of pokemon data
tests = open("data.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
data = json.load(tests)

import uuid

def Music(self, name, skill, type, health):
        self.name = name
        self.skill = skill
        self.type = type
        self.health = health

def create_Music(name, skill, type, health):
    new_Main = {
        "name" : name, 
        "skill": skill, 
        "type" : type, 
        "health" : health                     
    }
    
    return new_Main

add_more_users = "Y"
still_continue = input("Would you like to continue Y/N ").upper()

while add_more_users == still_continue:
    if add_more_users == "Y":
            still_continue
            name = input("Enter a name:")
            skill = input("Enter a work:")
            type = input("Enter year of their music:")
            health = 0
            new_Main_info = create_Music(name, skill, type, health)
            data.append(new_Main_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_users == "N":
          break

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")

data.append(data)