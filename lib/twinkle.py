import random
class Twinkle():
    def __init__(self, number, colour, rows, columns, offset=(0,0)):
        self.number = number
        self.colour = colour
        self.rows = rows
        self.columns = columns
        self.offset = offset
        self.overlay = []
        
    def calc_next_overlay(self):
        self.overlay=[]
        for x in range(0,self.number):
            self.overlay.append(((random.randint(0,self.rows-1), 
                              random.randint(0,self.columns-1)),self.colour))

            