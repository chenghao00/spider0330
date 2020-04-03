import random
import math

class Point:
    def __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)

class Straightline:
    def getlen(self,p1,p2):
        return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

p1=Point()
p2=Point()
s=Straightline()
line=s.getlen(p1,p2)
print(p1.x,p1.y,p2.x,p2.y,line)