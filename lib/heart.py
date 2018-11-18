
class Heart():
    
    def __init__(self):
        # r= red, p=pink to help make the arrays make more sense
        self.r=(30,0,0)
        self.p=(20,5,5)
        self.b=(0,0,0)
        self.rows=8
        self.columns=8
        self.small_heart=[[self.b, self.b, self.b, self.b, self.b, self.b, self.b, self.b,],
                          [self.b, self.r, self.r, self.b, self.r, self.r, self.b, self.b,],
                          [self.r, self.p, self.p, self.r, self.p, self.p, self.r, self.b,],
                          [self.r, self.p, self.p, self.p, self.p, self.p, self.r, self.b,],
                          [self.b, self.r, self.p, self.p, self.p, self.r, self.b, self.b,],
                          [self.b, self.b, self.r, self.p, self.r, self.b, self.b, self.b,],
                          [self.b, self.b, self.b, self.r, self.b, self.b, self.b, self.b,],
                          [self.b, self.b, self.b, self.b, self.b, self.b, self.b, self.b,]]
        self.big_heart=[[self.b, self.r, self.b, self.b, self.b, self.r, self.b, self.b,],
                          [self.r, self.p, self.r, self.b, self.r, self.p, self.r, self.b,],
                          [self.r, self.p, self.p, self.r, self.p, self.p, self.r, self.b,],
                          [self.r, self.p, self.p, self.p, self.p, self.p, self.r, self.b,],
                          [self.r, self.p, self.p, self.p, self.p, self.p, self.r, self.b,],
                          [self.b, self.r, self.p, self.p, self.p, self.r, self.b, self.b,],
                          [self.b, self.b, self.r, self.p, self.r, self.b, self.b, self.b,],
                          [self.b, self.b, self.b, self.r, self.b, self.b, self.b, self.b,]]
        # heartbeat pattern s= small, b=big
        self.pattern=["s","s","s","s","s","b","s","b"]
        self.pattern_posn = 0
        self.frame=[]
        
    def calc_next_frame(self):
        self.frame = []
        for x in range(0,self.rows):
            self.frame.append([])
            for y in range(0,self.columns):
                if self.pattern[self.pattern_posn] == "s":
                    self.frame[x].append(self.small_heart[x][y])
                else:
                    self.frame[x].append(self.big_heart[x][y])
        self.pattern_posn = (self.pattern_posn + 1) % 8