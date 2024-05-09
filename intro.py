narrator = ("Hello and welcome to the Hello Kitty Potion Game! You are Hello Kitty, and all of your friends have turned evil due to an unknown illness. You will need to compete with your friends in various competitions in order to obtain items for a blueberry potion. At the end of the forest you will find a potion that turns all your friends back to normal.")
start = (input("Do you wish to start a Sanrio memory game? Y/N: "))
def intro(start):
    for i in start:
        if start == "Y":
            print(narrator)
        elif start == "N":
            print("Exit Game. We hope to see you again!")
        else:
            print("Invalid")
            exit()
intro(start)


