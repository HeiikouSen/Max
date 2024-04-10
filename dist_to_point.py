import math

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def dist_to_point(self, Point):
        dist = math.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        return dist

p1 = Point(4,20)
p2 = Point(10,5)
print(p1.dist_to_point(p2))