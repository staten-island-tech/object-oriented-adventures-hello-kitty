narratorend = ("You have obtained all neccesary materials to save your friends.") 
end = ("You poured the solution, solute, and fairy dust into the magic bottle for the potion. After you mixed the solution with a branch, put the cork on top and shook it, then you  layed out the magic map and held it in place with magic rocks. Finally, the magic potion was poured on to the magic map and all of your friends were cured from the illness.")
start = (input("Do you wish to start a Sanrio memory game? Y/N: ")) 
congrats = ("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")

def conclusion(end):
    for i in end:
        if end == "Y":
            print(narratorend)
        elif end == "N":
            print("Congratulations you have completed the Hello Kitty Potion Game! Please tell your friends about it and exit the terminal.")
        else:
            print("Invalid")
conclusion(end)


#1st it will print out the end variable, it will congrtuate them for compeltitng the game then it will ask if the user wants to restart the game















#Maybe use while loop? 
#Do you want to play again Y/N
#If yes restart game. If No print end screen.
# The End.  
