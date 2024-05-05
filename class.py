from intro import narration
from intro import start
from middle import right
from middle import question
from middle import left
import intro
import middle

class Game:
    def intro(start):   
        for i in start:
            if start == "Y":
                print(narration)
            elif start == "N":
                print("Exit terminal.")
            else:
                print("Invalid")

    intro(start)

    while start == "Y": 
        def middle():         
            for i in range(4):
                question = input("Do you want to go left or right?:")
                if question == "left":
                    print("Safe")
                elif question == "right":
                    print("Game Over")
                    again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                    if again == "Yes":
                        middle()
                        return
                    if again == "No":
                        return
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
                    exit()
        
                while question == "left":
                    question = input("Do you want to go left or right?:")
                    if question == "right":
                        print("Safe")
                    elif question == "left":
                        print("Game Over")
                        again = input("Do you want to play again?: (Brings you back to questions) Yes or No:")
                        if again == "Yes":
                            middle()
                            return
                        if again == "No":
                            return
                        else:
                            print("Invalid")
                    else:
                        print("Invalid")
                        exit()
            while True:
                question = input("Are you ready to see what you got?: Yes or No?:")
                if question == "Yes":
                    print("Yay! You've made it! Take a cork to get a potion bottle!")
                    return
                elif question == "No":
                    print("Sorry, but I'm afraid this will leave you as incomplete.")
                    return
                else:
                    print("Invalid")
                    exit()
        middle()
        exit()
