
class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def scale(self, scale):
        self.x *= scale
        self.y *= scale

    def divide(self, scale):
        if scale == 0:
            raise ValueError("Can't divide by zero")
        self.x /= scale
        self.y /= scale

