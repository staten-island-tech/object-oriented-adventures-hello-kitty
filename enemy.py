class Friend:
   def __init__(self, name, skill):
      self.name = name
      self.skill = skill


class Friends(Friend):
   def __init__(self, name, skill):
      super().__init__(name, skill)
   def __str__(self):
      return f"{self.name}, {self.skill}"

friends = []

def create_friend(name, skill):
   her_friends = Friends(name, skill)
   friends.append(her_friends)
   for friend in friends:
      print(friend)

add_friend = "Y"

while add_friend == 'Y':
   request = input("Want to know who your friends are? Y or N:")
   if request == "Y":
      name = "Keroppi"
      skill = "Cooking"
      create_friend(name, skill)
      name = "Tuxedo Sam"
      skill = "Making Ties"
      create_friend(name, skill)
   else:
      print("Sorry, I'm afraid you can't play this game.")
      exit()
