from pgzero.actor import Actor


class Paddle:
    def __init__(self, x, y, sprite):
        self.actor = Actor(sprite, (x, y))

    def draw(self):
        self.actor.draw()

    def update_left(self):
        if self.actor.x - 4 > 0 + 48:
            self.actor.x = self.actor.x - 8

    def update_right(self):
        if self.actor.x + 4 < 640 - 48:
            self.actor.x = self.actor.x + 8
