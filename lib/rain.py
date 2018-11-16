import random

class Rain:
    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.current_frame = []
        self.raindrops = 10
        self.drops = []
        for drop in range(0, self.raindrops):
            self.drops.append([random.randint(2,self.rows-2), (random.randint(0, self.columns-1))])
        # c= cloud, r=rain, g=ground, s=sky
        # like this to make the grid make sense
        self.c = (10,10,10)
        self.r = (0,0,10)
        self.g = (0,10,0)
        self.s = (0,0,0)
        self.background = [[self.c,self.c,self.c,self.c,self.c,self.c,self.c,self.c],
                           [self.s,self.c,self.c,self.s,self.c,self.c,self.c,self.c],
                           [self.s,self.s,self.s,self.s,self.s,self.s,self.s,self.s],
                           [self.s,self.s,self.s,self.s,self.s,self.s,self.s,self.s],
                           [self.s,self.s,self.s,self.s,self.s,self.s,self.s,self.s],
                           [self.s,self.s,self.s,self.s,self.s,self.s,self.s,self.s],
                           [self.s,self.g,self.g,self.g,self.s,self.s,self.s,self.s],
                           [self.g,self.g,self.g,self.g,self.g,self.g,self.g,self.g]]

            
        self.frame = []
        for x in range(0,self.rows):
            self.frame.append([])
            for y in range(0,self.columns):
                self.frame[x].append(self.background[x][y])
        
        for drop in self.drops:
            self.frame[drop[0]][drop[1]] = self.r
        
    def calc_next_frame(self):
#        for x in range(0,self.rows):
#            for y in range(0,self.columns):
#                self.frame[x][y] = self.background[x][y]
#        self.frame = self.background[:]
        self.frame = []
        for x in range(0,self.rows):
            self.frame.append([])
            for y in range(0,self.columns):
                self.frame[x].append(self.background[x][y])
        
        for drop in self.drops:
            drop[0] = drop[0]+1
            if drop[0] > 6:
                drop[0]=2
                drop[1]=random.randint(0,self.columns-1)
            self.frame[drop[0]][drop[1]] = self.r
            
            
        
        