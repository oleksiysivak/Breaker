from pgzero.actor import Actor
from pgzero.game import screen

WIDTH = 640
HEIGHT = 480


class Ball:
    def __init__(self, x, y, speed_x, speed_y, sprite):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.actor = Actor(sprite, (x, y))
        self.screen = screen

    def draw(self):
        self.actor.draw()

    def update(self):
        self.actor.x += self.speed_x
        self.actor.y -= self.speed_y

        if (self.actor.x > WIDTH - 10) or (self.actor.x < 0 + 10):
            self.speed_x *= -1

        if self.actor.y < 0 + 10:
            self.speed_y *= -1

        # Game over if ball touches bottom of the screen
        if self.actor.y > HEIGHT - 10:
            return False

        return True

    def interact(self, paddle):
        if self.actor.colliderect(paddle.actor):
            self.speed_y *= -1
