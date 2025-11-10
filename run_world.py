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
    def __init__(self, size_x, size_y, total_rounds):
        self.size_x = size_x
        self.size_y = size_y
        self.total_rounds = total_rounds

        self.round = 0 # set the initial round to 0 

    def temporal(self): 
        if self.round % 2 == 0: 
            print("It's day!")
        else: 
            print("It's night")

    def next_round(self):
        if self.round < self.total_rounds:
            self.temporal() # print if day or night; print before incremention? how can i have a round 0? 
            self.round += 1 # increase 
        else: 
           print("The final round is complete. End of simulation.")

my_world = World(size_x=10, size_y=10, total_rounds=5)
my_world.next_round()
my_world.next_round()
my_world.next_round()

class Weather: 
  def __init__(self, time, sun, rain):
    self.time = time
    self.sun = sun
    self.rain = rain

class Cell: 
  def __init__(self, x, y, wet, sun, rain):
    # x and y position 
    # wet, sun, rain - boolean 
    pass

