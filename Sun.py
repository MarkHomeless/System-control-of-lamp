import math
import numpy as np
class Sun:
    def __init__(self, SEA, AZ):
        self.r = 100
        self.x = self.r * math.cos(SEA) * math.cos(AZ)
        self.y = self.r * math.cos(SEA) * math.sin(AZ)
        self.z = self.r * math.sin(SEA)
    def position(self):
        position = [self.x, self.y, self.z]
        return np.array(position) 
    def update_position(self, SEA, AZ):
        self.x = self.r * math.cos(SEA) * math.cos(AZ)
        self.y = self.r * math.cos(SEA) * math.sin(AZ)
        self.z = self.r * math.sin(SEA)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
