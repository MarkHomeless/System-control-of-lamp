import math
import numpy as np
class Flower:
    def __init__(self, x = None, y = None, z = None):
        if x is None:
            self.x = 0
        else:
            self.x = x
        if y is None:
            self.y = 0
        else:
            self.y = y
        if z is None:
            self.z = 0
        else:
            self.z = z
    def position(self):
        return np.array([self.x, self.y, self.z])
