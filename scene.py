import pgzrun
import time



# Class imports
from paddle import Paddle
from ball import Ball
from brick import Brick
TITLE = "Brickbreaker"
WIDTH = 640
HEIGHT = 480
BRICKS_PER_ROW = 10


paddle: Paddle
ball: Ball
bricks = []
is_game = True
is_victory = False
score = 0
start_time = time.time()




def init_game():
    global paddle, ball, bricks, is_game, is_victory, score

    paddle = Paddle(320, 440, "paddle.png")
    ball = Ball(320, 340, 3, 3, "ball.png")
    bricks = []
    place_bricks()

    is_game = True
    is_victory = False
    score = 0


# Create bricks (brick sprites are 64 by 32)
def place_brick_row(sprite, pos_x, pos_y, health_points):
    global bricks

    for i in range(BRICKS_PER_ROW):
        brick = Brick(pos_x + i * 64, pos_y, health_points, sprite)
        bricks.append(brick)


def place_bricks():
    brick_sprites = ["brick_green.png", "brick_red.png", "brick_blue.png"]
    current_brick_pos_x = 64 / 2
    current_brick_pos_y = 32 / 2
    health_points = len(brick_sprites)
    for brick_sprite in brick_sprites:
        place_brick_row(brick_sprite, current_brick_pos_x, current_brick_pos_y, health_points)
        current_brick_pos_y += 32
        health_points -= 1


init_game()


# Draw scene
def draw():
    
    if is_game:
        screen.fill((100, 149, 237))

        paddle.draw()
        ball.draw()
     
        for brick in bricks:
            brick.draw()
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        screen.draw.text(f"time: {elapsed_time:.2f}",[WIDTH-100 , HEIGHT-20 ], fontsize=30)
        
    else:
        screen.clear()
        if is_victory:
            #victory
            sounds.award.play()
            screen.fill((0, 127, 63))
            screen.draw.text("Victory", [WIDTH / 2 - 60, HEIGHT / 2], fontsize=50)
            
        else:
            #sound effect
            
            sounds.losing.play()
            
            screen.fill((127, 0, 63))
            screen.draw.text("Game Over", [WIDTH / 2 - 60, HEIGHT / 2], fontsize=50)
            
        screen.draw.text("Score: %i" % score, [WIDTH / 2 - 60, HEIGHT / 2 + 50], fontsize=30)
        screen.draw.text("Press space to restart", [WIDTH / 2 - 60, HEIGHT / 2 + 100], fontsize=30)


def update():
    global is_game, is_victory, score

    # Paddle update
    # 2 keyboard options
    if keyboard.left:
        paddle.update_left()
    if keyboard.right:
        paddle.update_right()
    if keyboard.d:
        paddle.update_right()
    if keyboard.a:
        paddle.update_left()

    if is_game:
        # Ball update
        is_game = ball.update()
        ball.interact(paddle)
        

        # Bricks update
        for brick in bricks:
            if ball.actor.colliderect(brick.actor):
                brick.healthPoints -= 1
                sounds.blip.play()
                if brick.healthPoints == 0:
                    bricks.remove(brick)
                score += 1
                ball.speed_y *= -1.05

        # If all bricks have been broken
        if not bricks:
            is_game = False
            is_victory = True
    else:
        if keyboard.space:
            init_game()


pgzrun.go()