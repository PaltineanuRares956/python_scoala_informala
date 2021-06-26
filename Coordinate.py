class Coordinate(object):
    """O coordonata e compusa din valorile x si y"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** (1/2)


origin = Coordinate(0, 0)
print(origin)
print(origin.x)
print(origin.y)
c1 = Coordinate(0, 1)
c2 = Coordinate(10, 20)

print(c1.distance(c2))