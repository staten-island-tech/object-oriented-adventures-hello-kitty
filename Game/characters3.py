import json
import os
# Open the JSON file of pokemon data

import uuid

def Music(self, name, skill, type, health):
    self.skill = skill
    self.name = name
    self.type = type
    self.health = health

def create_characteristics(name, skill, type, health):
    new_characteristics = {
        "name" : name,
        "skill" : skill,
        "type" : type,
        "health" : health
    }
    
    return new_characteristics

data = []

add_more_characteristics = "Y"
still_continue = input("Would you like to continue Y/N ").upper()

while add_more_characteristics == still_continue:
    if add_more_characteristics == "Y":
            still_continue
            name = input("Enter a name:")
            skill = input("Enter a work:")
            health = input("Enter year of their music:")
            type = input("Enter year of their music:")
            new_characteristics_info = create_characteristics(name, skill, health, type)
            data.append(new_characteristics_info)
    still_continue = input("Would you like to continue Y/N ").upper()       
    if add_more_characteristics == "N":
          break

new_file = "update.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("updated.json")
os.rename(new_file, "update.json")

data.append(data)