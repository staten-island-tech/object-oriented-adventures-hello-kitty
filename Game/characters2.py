def go_on():
    level_up = input("Do you want to proceed to the next level? Y or N:")
    for i in level_up:
        if level_up == "Y":
            print("Great! Let's move on!")
            return
        else:
            print("Invalid")
            exit()