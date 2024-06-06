def go_on():
  ask = input("Do you want to proceed to the next level? Y or N:")
  if ask.upper() == "Y":
        print("Great! Let's move on!")
        return
  else:
        print("Invalid")
        exit()