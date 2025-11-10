"""
The world
must have a temporal dimension (time goes by in rounds)
one round of day is followed by
one round of night
amount of rounds can be configured (0 – ∞)
must have 2 spatial dimensions (X/Y axis)
size of the world (length of Y/X axis) must be configurable
There should be events:
every day the sun is randomly shining in some places (cells) (based on a configurable probability between 100-0)
every day it rains in some random places (cells)
based on a configurable probability between 100-0
however when the sun is shining its x percent less likely that it rains
x is configurable
since the cells get wet, they stay wet over night and are only considered dried when the next day starts
for every cell/place on the grid at any moment we should be able to know about:
water that might be there,
sun that might be shining,
which cells are neighbors to it (left, right, top, bottom)
"""

class World:
    def __init__(self, name, size_x, size_y, total_rounds, probabilities):
        self.name = name
        self.size_x = size_x
        self.size_y = size_y
        self.total_rounds = total_rounds
        self.sun = probabilities[0]
        self.rain = probabilities[1]
        self.round = 0 # set the initial round to 0, it is night 

    def introduction(self): 
        print(f"Welcome! This is a simulation of the world '{self.name}'")
        
    def temporal(self): 
        if self.round % 2 == 0: 
            print(f"Round {self.round}: It's night!")
        else: 
            print(f"Round {self.round}: It's day!")

    def next_round(self):
        if self.round < self.total_rounds:
            self.round += 1 # increase 
            self.temporal()
        else: 
           print("The final round is complete. End of simulation.")

probabilities = [0.6, 0.4]
my_world = World(name = "Shire", size_x=10, size_y=10, total_rounds=5, probabilities=probabilities)
my_world.introduction()
my_world.next_round()
my_world.next_round()
my_world.next_round()
my_world.next_round()
my_world.next_round()
my_world.next_round()


class Cell: 
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.sun = False 
    self.rain = False
    self.wet = False
    
    def weather(self):
        self.sun = my_world.sun
        if my_world.round % 2 == 0:
            print("It is night. There is no sun nor rain.") # could later have it rain at night? 
        else: 
            if self.sun == False:
                self.rain = True 
                print("It is raining.")
            else:
                print("The sun is shining.")

    def is_wet(self):
        if self.wet == False: 
            print("The cell is dry.")
        elif (self.wet == True and self.sun == True):
            print("The cell has dried.")
        else: 
            print("The cell is and remains wet.")