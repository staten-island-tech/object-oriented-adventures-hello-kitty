import enemy 
import character

right = "<"
question = None
left = ">"

def attack():
    if character < enemy:
        return

def parts():
    for i in range(4): 
        question = input("Do you want to go left or right?")
        if question == "left":
            print("Safe")
        elif question == "right":
            attack
            print("Game Over")
            return
        
        while question == "left":
            question = input("Do you want to go left or right?")
            if question == "right":
                print("Safe")
            elif question == "left":
                attack
                print("Game Over")
                return

parts()   
