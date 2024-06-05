import json
import os
# Open the JSON file of pokemon data
tests = open("data.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
data = json.load(tests)

import uuid

def Music(self, work, name, year):
        self.work = work
        self.name = name
        self.year = year

def create_Music(name, work, year):
    new_Music = {
        "name" : name, 
        "work": work, 
        "year" : year,                      
    }
    
    return new_Music

data = []

add_more_users = "Y"
still_continue = input("Would you like to continue Y/N ").upper()

while add_more_users == still_continue:
    if add_more_users == "Y":
            still_continue
            name = input("Enter a name:")
            work = input("Enter a work:")
            year = input("Enter year of their music:")
            new_Music_info = create_Music(name, work, year)
            data.append(new_Music_info)
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