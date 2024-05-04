narration = ["You have obtained all neccesary materials to save your friend.--", "You poured the solution, solute, and fairy dust into the magic bottle for the potion.", "Then it was throughly mixed before it was corked and shaken.", "After, you lay out the magic map and hold it in place with magic rocks.", "Finally, the magic potion is poured on to the magic map and cures all of your friends from the infection."]
next = input("ENTER Next:")

def end():
    for i in range(1):
        if next == "Next":
            print(narration[0])
            print(narration[1])
            print(narration[2])
            print(narration[3])
            print(narration[4])
        else:
            return

end()
