characters and enemies from import sanrio_characters

right = "<"
question = None
left = ">"

def middle():
    def attack():
        if character < enemy and character > enemy:
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

        question = input("Are you ready to see what you got?")
        if question == "Yes":
            print("Yay! You've made it! Take a cork to get a potion bottle!")
        elif question == "No":
            print("Sorry, but I'm afraid this will leave you as incomplete?")
    parts()

middle()
