import numpy as np
import random 

class Cloude:
    def __init__(self, speed_of_wind = None):
        self.center = [random.randint(-30,30), random.randint(-30,20), random.randint(5, 15)]
        self.x_offset = random.randint(2,10)
        self.y_offset = random.randint(2,7)
        self.x1 = self.x2 = self.center[0]+self.x_offset
        self.x3 = self.x4 = self.center[0]-self.x_offset
        self.y1 = self.y3 = self.center[1]+self.y_offset
        self.y2 = self.y4 = self.center[1]-self.y_offset
        self.z1 = self.z2 = self.z3 = self.z4 = self.center[2]
        if speed_of_wind is None:
            self.speed_of_wind_x = random.randint(-2, 2)
            self.speed_of_wind_y = random.randint(-2, 2)
            self.speed_of_wind_z = 0
        else:
            self.speed_of_wind_x = speed_of_wind[0]
            self.speed_of_wind_y = speed_of_wind[1]
            self.speed_of_wind_z = speed_of_wind[2]
    def position(self):
        return np.array([[self.x1, self.y1,self.z1],  [self.x2, self.y2,self.z2], 
                         [self.x3, self.y3,self.z3],  [self.x4, self.y4,self.z4] ])
    def get_x(self):
        return [self.x1, self.x2, self.x3, self.x4]
    def get_y(self):
        return [self.y1, self.y2, self.y3, self.y4]
    def get_z(self):
        return [self.z1, self.z2, self.z3, self.z4]
    def center_position(self):
        return np.array(self.center)
    def move(self):
        self.center[0] = self.center[0]+self.speed_of_wind_x
        self.x1 = self.x1 + self.speed_of_wind_x
        self.x2 = self.x2 + self.speed_of_wind_x
        self.x3 = self.x3 + self.speed_of_wind_x
        self.x4 = self.x4 + self.speed_of_wind_x
        
        self.center[1] = self.center[1]+self.speed_of_wind_y
        self.y1 = self.y1 + self.speed_of_wind_y
        self.y2 = self.y2 + self.speed_of_wind_y
        self.y3 = self.y3 + self.speed_of_wind_y
        self.y4 = self.y4 + self.speed_of_wind_y
        
        self.center[2] = self.center[2]+self.speed_of_wind_z
        self.z1 = self.z1 + self.speed_of_wind_z
        self.z2 = self.z2 + self.speed_of_wind_z
        self.z3 = self.z3 + self.speed_of_wind_z
        self.z4 = self.z4 + self.speed_of_wind_z
    def check_out_of_sight(self,x_sight, y_sight):
        if (x_sight<self.center[0] or self.center[0]<-x_sight) or (y_sight<self.center_position()[1] or self.center_position()[1]<-y_sight):
            return True
        return False 
