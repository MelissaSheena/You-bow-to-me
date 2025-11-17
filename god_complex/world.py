"""
Class World: 
this class is in control of everything 
- weather 
- finding neighbours
"""

import random # to get randomised situation 
from cells import Cell

class World:
    def __init__(self, name, size_x, size_y, total_rounds, sunny_prob, rainy_prob, rws_factor):
        self.name = name
        self.size_x = size_x
        self.size_y = size_y
        self.total_rounds = total_rounds
        self.sunny = sunny_prob
        self.raining = rainy_prob
        self.rws = rws_factor # the factor by which the chance of rain decreases when the sun shines 
        self.round = 0 # starts at night  
        self.grid = self.create_grid() # call function from class 

    def introduction(self): 
        print(f"Welcome! This is a simulation of the world '{self.name}'")
    
    def create_grid(self):
        grid = []
        for y in range(self.size_y):
            row = []
            for x in range(self.size_x):
                row.append(Cell(x,y))
            grid.append(row)
        return grid # to access the cell, use self.grid[y][x]

    def temporal(self): 
        if self.round % 2 == 0: 
            print(f"Round {self.round}: It's night!")
            self.night()
        else: 
            print(f"Round {self.round}: It's day!")
            self.day()

    def next_round(self):
        if self.round >= self.total_rounds:
            print("The final round is complete. End of simulation.")
            return
            
        self.round += 1 # increase 
        self.temporal()

    
    def day(self):
        # before checking the weather, the cells need to dry
        for row in self.grid:
            for cell in row: 
                cell.night_to_day()
    
        self.weather() # get weather conditions for each cell

    def night(self):
        for row in self.grid:
            for cell in row:
                cell.wet_overnight() 

    def weather(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                cell = self.grid[y][x]

            # check whether the sun is shining, if not, it rains  
            rain_prob = self.raining
            if random.randint(0,100) < self.sunny:# get random probability and check with sun probabiltiy 
                cell.sunny(True)
                rain_prob = self.raining * (1-self.rws / 100)
            
            if random.randint(0,100) < rain_prob:
                cell.raining(True)

    def neighbours(self, cell):
        """To get the neighbours of a specific cell
                    (x, y-1)
        (x-1, y)    (x,y)       (x+1, y)
                    (x, y+1)
        """
        neighbours = {} # initiate dictionary 
        x,y = cell.x, cell.y # get cell location 

        # left 
        if x > 0: 
            neighbours['left'] = self.grid[y][x-1]
        
        # right
        if x < self.size_x -1: 
            neighbours['right'] = self.grid[y][x+1]

        # up 
        if y > 0: 
            neighbours['up'] = self.grid[y-1][x]

        # down 
        if y < self.size_y-1: 
            neighbours['down'] = self.grid[y+1][x]

        return neighbours 
    
    def get_cell_state(self, x, y):
        cell = self.grid[y][x]
        state = {}
        state.update({'position': (x,y), 'is_sunny': cell.sun, 'is_rainy': cell.rain, 
                      'is_wet': cell.wet, 'neighbours': self.neighbours(cell)})
        return state

    def run_simulation(self):
        self.introduction()
        while self.round < self.total_rounds:
            self.next_round()
    