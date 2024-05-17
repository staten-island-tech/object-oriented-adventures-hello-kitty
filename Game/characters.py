import intro
def part1():
  next = input("Welcome! You've entered Level 1! Want to see your first opponent? Y or N:")
  for i in range(1):
      if next == "Y":
          name = "My Melody"
          skill = "Handstand endurance"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You've come across My Melody.")
      else:
          print("Invalid")
          exit()

  while next == "Y":
    move_on = input("My Melody does a handstand for 20 minutes. How long would you do one?: 25 minutes?(L) or 20 minutes(R):")
    for i in range(1):
      if move_on == "L":
          name = "Hello Kitty"
          skill = "Battling"
          type = "Hero"
          main = "Main character"
          health = 15
          print(name, skill, type, main, health)

          name = "My Melody"
          skill = "Handstand endurance"
          type = "Enemy"
          status2= "Infected"
          health = 0
          print(name, skill, type, status2, health)
          print("You have successfully made through Level 1, with an addition of a solute for yout potion!")
      else:
          print("Invalid")
          again = input("Do you want to start all over again?: Yes or No:")
          if again == "Yes":
              intro
          else:
              print("Good Bye!")
              exit()

    while move_on == "L":
       level_up = input("Do you want to proceed to the next level? Y or N:")
       for i in range(1):
          if level_up == "Y":
              print("Great! Let's move on!")
              return
          else:
              print("Invalid")
              exit()
part1()
