narration = ("Hello and welcome to the Hello Kitty Potion Game! You are Hello Kitty, and all of your friends have turned evil due to an unknown illness. You will need to compete with your friends in various competitions in order to obtain items for a blueberry potion. At the end of the forest you will find a potion that turns all your friends back to normal.")
import classes
import characters2
import uuid

class function():
    def __init__(self, ask):
        self.ask = ask

class introduction(function):
    def __init__(self, ask, start):
        super().__init__(ask)
        self.start = start
    def __str__(self):
        return f"{self.start}, {self.ask}"
    
class parts(function):
    def __init__(self, ask, move, again):
        super().__init__(ask)
        self.move = move
        self.again = again
    def __str__(self):
        return f"{self.ask}, {self.move}, {self.again}"

class conclusion(function):
    def __init__(self, ask, question):
        super().__init__(ask)
        self.question = question
    def __str__(self):
        return f"{self.ask}, {self.question}

intros = []
parts = []
conclusions = []

def create_introduction(ask, start):
    introd = Intro(ask, start)
    intros.append(introd)
    for intro in intros:
        print(intro)

def create_parts(ask, move, again):
    part_s = Parts(ask, move, again)
    parts.append(part_s)
    for part in parts:
        print(part) 
    
def create_conclusion(ask, question):
    conclude = Conclude(ask, question)
    conclusions.append(conclude)
    for conclusion in conclusions:
        print(conclusion) 

user_request = "Y"
        
def check_tenure(status):
    if status.lower() == "Y":
        return True
    else:
        return False
