import random

class Flame:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.current_frame = []
        self.next_frame = []
        self.countdown = 0
        self.flare = 0
        self.margin=2

        self.flame_lowers = [[0, 0, 440, 700, 700, 440, 0, 0], 
                             [0, 0, 100, 300, 300, 100, 0, 0]]
        self.flame_uppers = [[0, 0, 700, 800, 800, 700, 0, 0], 
                             [0, 0, 200, 350, 350, 200, 0, 0]]
               
        self.flame_cols = 2
        
        self.frame_temps = []
        
        # initialise matrix sizes
        for x in range(0, self.rows):
            self.current_frame.append([])
            self.next_frame.append([])
            self.frame_temps.append([])
            for y in range(0, self.cols):
                self.current_frame[x].append(0)
                self.next_frame[x].append(0) 
                self.frame_temps[x].append(0)
        
    def calc_next_frame(self):
            
        if self.countdown == 0:
            print(self.countdown)
            self.countdown = 10
            self.flare = random.randint(100, 170)
        self.countdown = self.countdown - 1

        # blank next_frame
        for x in range(0, self.rows):
            for y in range(self.flame_cols, self.cols):
                self.next_frame[x][y] = 0
    
        # add the random flame pattern
        for x in range(0, self.rows):
            for y in range(0, self.flame_cols):
                self.next_frame[x][y] = random.randint(
                                self.flame_lowers[y][x], 
                                self.flame_uppers[y][x])

        # now itteate the heat up
        for x in range(self.margin, self.rows-self.margin):
            for y in range(1, self.cols):
                self.next_frame[x][y] = self.next_frame[x][y] + (self.current_frame[x][y-1]) - self.flare
                self.frame_temps[x][y] = self.rgb_from_temp(self.next_frame[x][y])
            self.frame_temps[x][0] = self.rgb_from_temp(self.next_frame[x][0])
                
        self.current_frame = self.next_frame
        

    def rgb_from_temp(self, temp):
        if temp < 400:
            return (0, 0, 0)
        elif temp < 700:
            return (int((temp-400)//10), 0, 0)
        elif temp < 1000:
            return (70, int((temp-700)/10), 0)
        else:
            return (100, 50, int((temp-1000)/15))