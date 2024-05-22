def go_on():
    level_up = input("Do you want to proceed to the next level? Y or N:")
    for i in range(1):
          if level_up == "Y":
              print("Great! Let's move on!")
              return
          else:
              print("Invalid")
              exit()