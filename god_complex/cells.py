""""
Class Cell
A cell should know 
- state [0 = dry, 1 = wet]
- its position 
"""

class Cell: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sun = False # is sun shining on it 
        self.rain = False # is it being rained on
        self.wet = False # is it stil wet from the day before? 
    
    # set status based on weather in world 
    def set_sun(self, sunny):
        self.sun = sunny
    
    def set_rain(self, raining):
        self.rain = raining 

    def wet_overnight(self):
        """ If it rained today, the cell will be wet tonight."""
        if self.rain:
            self.wet = True 

    def night_to_day(self):
        self.wet = False 


