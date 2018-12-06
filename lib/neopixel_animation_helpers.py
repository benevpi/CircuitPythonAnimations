import time

class Spiral():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        
    def convert_xy_to_index(self, row, col):
        return (row*self.rows) + col
        
class ZigZagMatrix():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        
    def convert_xy_to_index(self, row, col):
        if row % 2 == 0:
            return (row*8)+col
        else:
            return ((row+1)*8)-(col+1)
       
class Timer():

    def __init__(self, fps, callback):
        self.fps = fps
        self.wait_seconds = (1/self.fps)
        self.done_one_loop = False
        self.callback = callback
        
        self.last_frame = time.monotonic()
        
    def check_timer(self):
        self.now = time.monotonic()
        if self.now > self.last_frame + self.wait_seconds:
            if not self.done_one_loop:
                print("Missed frame deadline")
            self.last_frame = time.monotonic()
            self.callback()
        self.done_one_loop = True

#overlay format[((x,y), (r,g,b))]
def apply_overlay(frame, overlay):
    for pixel in overlay:
        frame[pixel[0][0]][pixel[0][1]] = pixel[1]
    
        
        
        
    