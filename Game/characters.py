import characters2
import json
import os
#Run this file to play the game.

# Open the JSON file of pokemon data
class characters:
    def __init__(self, name, skill, type, health):
        self.name = name
        self.skill = skill    
        self.type = type
        self.health = health
    
    def decrease_strength(self, value_to_decrease):
        self.health -= value_to_decrease
    
    def increase_strength(self, value_to_increase):
        self.health += value_to_increase

    def update_status(self, new_health):
        self.health = new_health

class Main_characters(characters):
    def __init__(self, name, skill, type, main, health):
        super().__init__(name,skill, type, health)
        self.main= main
    def __str__(self):
      return f"{self.name},{self.skill},{self.type}, {self.main}, {self.health}"
class friends_lst(characters):
    def __init__(self, name, skill, type, status2, health):
        super().__init__(name,skill, type, health)
        self.status2 = status2
    def __str__(self):
      return f"{self.name}, {self.skill},{self.type}, {self.status2}, {self.health}"
class Enemy(characters):
    def __init__(self, name, skill, type, status1, health):
        super().__init__(name,skill, type, health)
        self.status1 = status1
    def __str__(self):
            return f"{self.name}, {self.skill},{self.type}, {self.status1}, {self.health}"

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
        "main" : main,
        "health" : health
    }
    return MAIN

def create_enemies(name, skill, type, health, status1):
    enemies = {
        "name" : name,
        "skill" : skill,
        "type" : type,
        "status1" : status1,
        "health" : health
    }
    return enemies

def create_friends(name, skill, type, health, status2):
    friends = {
        "name" : name,
        "skill" : skill,
        "type" : type,
        "status2" : status2,
        "health" : health
    }
    return friends

data = []

def check_stat(stat): #This checks the status to see if the user put Y or not.
    if stat.lower == "y":
        return True
    else:
        return False
 
class Game: 
    def __init__(self, ask):
            self.ask = ask
    
    def __init__(self, ask, start):
            super().__init__(ask)
            self.start = start
    def __str__(self):
            return f"{self.start}, {self.ask}"
  
    def beginning():
        start = input("Do you want to play a Sanrio memory game? Y/N:")
        if start.upper() == "Y":
            print("Hello and welcome to the Hello Kitty Potion Game! You are Hello Kitty, and all of your friends have turned evil due to an unknown illness. You will need to compete with your friends in various competitions in order to obtain items for a blueberry potion. At the end of the forest you will find a potion that turns all your friends back to normal.")
        elif start.upper() == "N":
            print("Exit terminal.")
            exit()
        else:
            print("Invalid")
            exit()
        characters2.go_on()
    beginning()

    user_request = input("Do you want to see the main character? Y/N: ")
    if user_request == "Y":
        mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
        print(mc)
    elif user_request == "N":
        print("Bye!")
        exit()
    else:
        print("Invalid")
        exit()
 
    def __init__(self, ask, move, still_continue):
            super().__init__(ask)
            self.move = move
            self.still_continue = still_continue
    def __str__(self):
            return f"{self.ask}, {self.move}, {self.still_continue}"
    
    def middle():
        still_continue = input("Welcome! You've entered Level 1! Want to see your opponent? Y or N:").upper()
        My_Melody = Enemy("My Melody", "Handstand", "Enemy", "Infected", 25 )
        print(My_Melody)
        if still_continue == "Y":
            name = "My Melody"
            skill = "Handstand endurance"
            type = "Enemy"
            status1 = "Infected"
            health = 25
            create_enemies(name, skill, type, status1, health)
            new_info = create_enemies(name, skill, type, status1, health)
            data.append(new_info)
        else:
            print("Invalid")
            exit()
           
        still_continue = input("Would you like to continue Y/N ").upper()
        if still_continue == "Y":
            move = input("My Melody does a handstand for 20 minutes. How long would you do one?: 25 minutes?(L) or 20 minutes(R):")
            if move == "L":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                main = "Main Character"
                health = 12.5
                create_main(name, skill, type, main, health)
                new_info = create_main(name, skill, type, main, health)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                mc.update_status("12.5")
                print(f" Battle Won!! Health: {mc.health}")
                print("Good job!! You have made it through with an addition of  magic dust.")
            elif move == "R":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                main = "Main Character"
                health = 0
                create_main(name, skill, type, main, health)
                new_info = create_main(name, skill, type, main, health)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                print(mc)
                print(f" Lost battle. Health: {mc.health}")
                exit()
            else:
                print("Invalid")
                exit()
        else:
            print("Invalid")
            exit()
            
    characters2.go_on()
    middle()
    
    def middle_cont():
        move = input("My Melody has returned stronger and does a handstand for 60 minutes. How long would you do one?: 90 minutes?(L) or 50 minutes(R):")
        My_Melody = Enemy("My Melody", "Handstand", "Enemy", "Infected", 25 )
        My_Melody.increase_strength(10)
        print(My_Melody)
        if move == "L":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 25
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
            mc.update_status("25")
            print(f" Battle Won!! Health: {mc.health}")
            print("You have successfully made through Level 1, with an addition of a solute for your potion!")
        elif move == "R":
            mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
            print(mc)
            print(f" Lost battle. Health: {mc.health}")
            exit()
        else:
            print("Invalid")

    characters2.go_on()
    middle_cont()

    def middle2():
        still_continue = input("Welcome! You've entered Level 2! Want to see your opponent? Y or N:").upper()
        Mimmy = Enemy("Mimmy", "Swimming", "Enemy", "Infected", 25 )
        print(Mimmy)
        if still_continue == "Y":
            name = "Mimmy"
            skill = "Swimming"
            type = "Enemy"
            health = 25
            status1 = "Infected"
            create_enemies(name, skill, type, health, status1)
            new_info = create_enemies(name, skill, type, health, status1)
            data.append(new_info)
            move = input("Mimmy does karate for 10 minutes. How long would you do one?: 50 minutes?(L) or 20 minutes(R):")
            if move == "L":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                health = 37.5
                main = "Main Character"
                create_main(name, skill, type, health, main)
                new_info = create_main(name, skill, type, health, main)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 37.5) 
                mc.update_status( "37.5")
                print(f" Battle Won!! Health: {mc.health}")
                print("Good job!! You have made it through with an addition of  magic dust.")
            elif move == "R":        
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                print(mc)
                print(f" Lost battle. Health: {mc.health}")
                exit()
            else:
                print("Invalid")
                exit()
        else:
            print("Invalid")
            exit()

    characters2.go_on()
    middle2()
          
    def middle2_cont():
        move = input("Mimmy comes back stronger and does karate for 20 minutes. How long would you do one?: 10 minutes?(L) or 30 minutes(R):")
        Mimmy = Enemy("Mimmy", "Swimming", "Enemy", "Infected", 25 )
        Mimmy.increase_strength(20)
        print(Mimmy)
        if move == "R":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 50
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
            mc.update_status("50")
            print(f" Battle Won!! Health: {mc.health}")
            print("You have successfully made through Level 2, with an addition of a solvent for your potion!")
        elif move == "L":
            mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
            print(mc)
            print(f" Lost battle. Health: {mc.health}")
            exit()
        else:
            print("Invalid")
            exit()

    characters2.go_on()
    middle2_cont()

    def middle3():
        still_continue = input("Welcome! You've entered Level 3! Want to see your opponent? Y or N:").upper()
        Pompompurin = Enemy("Pompompurin", "Bubble Gum Competition", "Enemy", "Infected", 25 )
        print(Pompompurin)
        if still_continue == "Y":
            name = "Pompompurin"
            skill = "Bubble Gum Competition"
            type = "Enemy"
            health = 25
            status1 = "Infected"
            create_enemies(name, skill, type, health, status1)
            new_info = create_enemies(name, skill, type, health, status1)
            data.append(new_info)
            move = input("Pompompurin chews bubble gum for breaking record of 55 minutes. How long would you do one?: 55 minutes(R) or 65 minutes(L):")
            if move == "L":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                health = 62.5
                main = "Main Character"
                create_main(name, skill, type, health, main)
                new_info = create_main(name, skill, type, health, main)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 62.5) 
                mc.update_status( "62.5") 
                print(f" Battle Won!! Health: {mc.health}")
                print("You have successfully made through the battle with an addition of Magic Rocks!")
            elif move == "R":
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                print(mc)
                print(f" Lost battle. Health: {mc.health}")
                exit()
            else:
                print("Invalid")
                exit()
        else:
            print("Invalid")
            exit()

    characters2.go_on()
    middle3()
    
    def middle3_cont():
        move = input("Pompompurin once again breaks the record by chewing bubble gum for 70 minutes. How long would you do one?: 75 minutes(R) or 65 minutes(L):")
        Pompompurin = Enemy("Pompompurin", "Bubble Gum Competition", "Enemy", "Infected", 60)
        Pompompurin.increase_strength(20)
        print(Pompompurin)
        if move == "R":
            name = "Hello Kitty"
            skill = "Battling"
            type = "Hero"
            main = "Main Character"
            health = 75
            create_main(name, skill, type, main, health)
            new_info = create_main(name, skill, type, main, health)
            data.append(new_info)
            mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
            mc.update_status("75")
            print(f" Battle Won!! Health: {mc.health}")
            print("You have successfully made through Level 3!")
            
        elif move == "L":
            mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
            print(mc)
            print(f" Lost battle. Health: {mc.health}")
            exit()
        else:
            print("Invalid")

    characters2.go_on()
    middle3_cont()

    def middle4():
        still_continue = input("Welcome! You've entered Level 4! Want to see your opponent? Y or N:").upper()
        Keroppi = Enemy("Keroppi", "Cooking", "Friend", "Infected", 80 )
        print(Keroppi)
        if still_continue == "Y":
            still_continue
            name = "Keroppi"
            skill = "Cooking"
            type = "Friend"
            health = 80
            status2 = "Uninfected"
            create_friends(name, skill, type, health, status2)
            new_info = create_friends(name, skill, type, health, status2)
            data.append(new_info)
            move = input("Keroppi is willing to be on your side. Will you accept him?: Yes(R) or No(L):")
            if move == "R":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                health = 79.25
                main = "Main Character"
                create_main(name, skill, type, health, main)
                new_info = create_main(name, skill, type, health, main)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                mc.update_status("79.25")
                print(f" Friend gained. Health: {mc.health}")
                print("Keroppi: I am so happy to be back with you. I think we have another friend to find, but I don't know who they may be.")
                print("You have successfully made through Level 4, with an addition of a Magic Map of the forest!")
            elif move == "L":
                print("Game cannot proceed without accepting friends.")
                exit()
            else:
                print("Bye!")
                exit()
        else:
            print("Invalid")
            exit()

    characters2.go_on()
    middle4()

    def middle5():
        still_continue = input("Welcome! You've entered Level 5! Want to see your opponent? Y or N:").upper()
        Kuromi = Enemy("Kuromi", "Swimming", "Enemy", "Infected", 85 )
        print(Kuromi)
        if still_continue == "Y":
            name = "Kuromi"
            skill = "Swimming"
            type = "Enemy"
            health = 85
            status1 = "Infected"
            create_enemies(name, skill, type, health, status1)
            new_info = create_enemies(name, skill, type, health, status1)
            data.append(new_info)
            move = input("Kuromi swims to the other end of a river in 35 minutes. How long would you do one?: 30 minutes?(R) or 40 minutes(L):")
            if move == "R":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                health = 85.75
                main = "Main Character"
                create_main(name, skill, type, health, main)
                new_info = create_main(name, skill, type, health, main)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                mc.update_status("85.75")
                print(f" Friend gained. Health: {mc.health}")
                print("You have successfully made through Level 5, with an addition of a Magic Bag!")
            elif move == "L":
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                print(mc)
                print(f" Lost battle. Health: {mc.health}")
                exit()
            else:
                print("Bye!")
                exit()
        else:
            print("Invalid")
            exit()

    characters2.go_on()
    middle5()  

    def middle6():
        still_continue = input("Welcome! You've entered Level 6! Want to see your opponent? Y or N:").upper()
        Pochacco = Enemy("Pochacco", "Bird Nest Making", "Enemy", "Infected", 90 )
        print(Pochacco)
        if still_continue == "Y":
            name = "Pochacco"
            skill = "Bird Nest Making"
            type = "Enemy"
            health = 90
            status1 = "Infected"
            create_enemies(name, skill, type, health, status1)
            new_info = create_enemies(name, skill, type, health, status1)
            data.append(new_info)
            move = input("Pochacco makes a bird nest in 25 minutes. How long would you do one?: 20 minutes?(L) or 30 minutes(R):")
            if move == "L":
                name = "Hello Kitty"
                skill = "Battling"
                type = "Hero"
                health = 92
                main = "Main Character"
                create_main(name, skill, type, health, main)
                new_info = create_main(name, skill, type, health, main)
                data.append(new_info)
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                mc.update_status("92")
                print(f" Battle successful!! Health: {mc.health}")
                print("You have successfully made through Level 6, with an addition of a bottle for your potion!")
            elif move =="R":
                mc = Main_characters("Hello Kitty", "Battling", "Main Character", "Hero", 0)
                print(mc)
                print(f" Lost battle. Health: {mc.health}")
                exit()
            else:
                print("Bye!")
                exit()
        else:
            print("Invalid")
            exit()

    characters2.go_on()
    middle6()  

    def __init__(self, ask, result):
            super().__init__(ask)
            self.result = result
    def __str__(self):
            return f"{self.ask}, {self.result}"
 
    def end():
        result = input("Do you want to see what had happened? Y or N:")
        if result.upper() == "Y":
            print("You have obtained all necessary materials to save your friends.","You poured the solution, solute, and fairy dust into the magic bottle for the potion. After you mixed the solution with a branch, put the cork on top and shook it, then you  layed out the magic map and held it in place with magic rocks. Finally, the magic potion was poured on to the magic map and all of your friends were cured from the illness.")
        elif result.upper() == "N":
            print("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")
            exit()
        else:
            print("Invalid")
            exit()
   
        ask = input("Ready to leave?: Y or N:")
        if ask == "Y":
            print("Sure was a good time. Hope to see you again! He-he-he!")
        elif ask == "N":
            print("Looks like one is here for more adventure!")
   
    end()

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("update.json")
os.rename(new_file, "updated.json")

data.append(data)