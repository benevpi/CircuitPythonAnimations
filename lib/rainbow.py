import random

class Rainbow():

    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.current_frame = []
        self.raindrops = 5
        self.droprange=3
        self.drops = []
        for drop in range(0, self.raindrops):
            self.drops.append([random.randint(2,self.rows-2), (random.randint(0, self.droprange))])
        # c= cloud, r=rain, g=ground, s=sky, u=sun (well, s was taken)
        # like this to make the grid make sense
        self.c = (5,5,5)
        self.r = (0,0,10)
        self.g = (0,10,0)
        self.s = (0,0,0)
        self.u = (70,50,0)
        self.r1 = (50,0,0)
        self.r2 = (70,30,0)
        self.r3 = (35,0,70)
        self.background = [[self.c,self.c,self.c,self.c,self.s,self.u,self.u,self.u],
                           [self.s,self.c,self.c,self.r3,self.r3,self.s,self.u,self.u],
                           [self.s,self.s,self.s,self.r2,self.r2,self.r3,self.s,self.s],
                           [self.s,self.s,self.s,self.r1,self.r1,self.r2,self.r3,self.s],
                           [self.s,self.s,self.s,self.s,self.s,self.r1,self.r2,self.r3],
                           [self.s,self.s,self.s,self.s,self.s,self.r1,self.r2,self.r3],
                           [self.s,self.g,self.g,self.g,self.s,self.g,self.g,self.g],
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
                drop[1]=random.randint(0,self.droprange-1)
            self.frame[drop[0]][drop[1]] = self.r
            
            
        
        