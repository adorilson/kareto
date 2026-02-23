class World:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height