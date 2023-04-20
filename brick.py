from pgzero.actor import Actor


class Brick:
    def __init__(self, x, y, health_points, sprite):
        self.healthPoints = health_points
        self.actor = Actor(sprite, (x, y))

    def draw(self):
        self.actor.draw()
