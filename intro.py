narrator = ("You are Hello Kitty. All of your friends have turned evil due to an unknown illness! You need to compete with your friends in competitions inorder to obtain items for the potion.At the end of the forest you will find a potion that turns all your friends back to normal.")
start = (input("Do you wish to start a Sanrio memory game? Y/N: "))
def intro(start):
    for i in start:
        if start == "Y":
            print(narrator)
        elif start == "N":
            print("Exit Game. We hope to see you again!")
        else:
            print("Invalid")
intro(start)
