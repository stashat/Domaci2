import math


class Line:
  
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
  
  def distance(self):
      return math.sqrt((self.x1 - self.x2)**2 + (self.y1-self.y2)**2)
  def slope(self):
      return (y2-y1)/(x2-x1)

x1=int(input('Unesite x1:'))
y1=int(input('Unesite y1:'))
x2=int(input('Unesite x2:'))
y2=int(input('Unesite y2:'))

line_1 = Line(x1,y1,x2,y2)
print((line_1.x1, line_1.y1), (line_1.x2, line_1.y2))
print(line_1.distance())
print(line_1.slope())


