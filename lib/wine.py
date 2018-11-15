
class Wine():
    def __init__(self):
        self.w = (50,50,50)
        self.r = (50,0,20)
        self.b = (0,0,0)
        self.full_glass = [[self.b,self.b,self.b,self.b,self.b,self.b,self.b,self.b],
                      [self.b,self.w,self.b,self.b,self.b,self.w,self.b,self.b],
                      [self.b,self.w,self.r,self.r,self.r,self.w,self.b,self.b],
                      [self.b,self.w,self.r,self.r,self.r,self.w,self.b,self.b],
                      [self.b,self.b,self.w,self.r,self.w,self.b,self.b,self.b],
                      [self.b,self.b,self.b,self.w,self.b,self.b,self.b,self.b],
                      [self.b,self.b,self.b,self.w,self.b,self.b,self.b,self.b],
                      [self.b,self.w,self.w,self.w,self.w,self.w,self.b,self.b]]
                      
        self.tipped_empty = [[self.b,self.b,self.b,self.w,self.b,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.w,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.w,self.b,self.b],
                            [self.w,self.b,self.b,self.b,self.b,self.w,self.b,self.b],
                            [self.b,self.w,self.b,self.b,self.b,self.w,self.b,self.b],
                            [self.b,self.b,self.w,self.w,self.w,self.w,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.w,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.b,self.w]]
        
        self.tipped_full = [[self.b,self.b,self.b,self.w,self.b,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.w,self.b,self.b,self.b],
                            [self.r,self.r,self.r,self.r,self.r,self.w,self.b,self.b],
                            [self.w,self.r,self.r,self.r,self.r,self.w,self.b,self.b],
                            [self.b,self.w,self.r,self.r,self.r,self.w,self.b,self.b],
                            [self.b,self.b,self.w,self.w,self.w,self.w,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.w,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.b,self.w]]
                            
        self.tipped_emptying1 = [[self.b,self.b,self.b,self.w,self.b,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.w,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.w,self.b,self.b],
                            [self.w,self.r,self.r,self.r,self.r,self.w,self.b,self.b],
                            [self.b,self.w,self.r,self.r,self.r,self.w,self.b,self.b],
                            [self.b,self.b,self.w,self.w,self.w,self.w,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.w,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.b,self.w]]
                            
        self.tipped_emptying2 = [[self.b,self.b,self.b,self.w,self.b,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.w,self.b,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.w,self.b,self.b],
                            [self.w,self.b,self.b,self.b,self.b,self.w,self.b,self.b],
                            [self.b,self.w,self.r,self.r,self.r,self.w,self.b,self.b],
                            [self.b,self.b,self.w,self.w,self.w,self.w,self.b,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.w,self.b],
                            [self.b,self.b,self.b,self.b,self.b,self.b,self.b,self.w]]
                            
        self.animation=[self.full_glass, self.tipped_full, self.tipped_emptying1, self.tipped_emptying2, self.tipped_empty]

        self.position = 0
        
        self.frame = self.animation[self.position]
                
    def calc_next_frame(self):
        self.position = (self.position + 1)%5
        self.frame = self.animation[self.position]
                      
