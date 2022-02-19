import turtle
from turtle import *
import time
import random

# This file will contain 3 classes : Body, Target, and Score

# ---------CLASS BODY-----------------
INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]


class Body:
    def __init__(self):
        self.total_parts = []
        self.create()

    def create(self):
        for pos in INITIAL_POS:
            self.add(pos)

    def add(self, pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.total_parts.append(snake)

    def grow(self):
        self.add(self.total_parts[-1].position())

    def move(self):
        for square in range(len(self.total_parts) - 1, 0, -1):
            y = self.total_parts[square - 1].ycor()
            x = self.total_parts[square - 1].xcor()
            self.total_parts[square].goto(x, y)
        self.total_parts[0].forward(20)

    # Changing the directions
    def up(self):
        if self.total_parts[0].heading() != 270:
            self.total_parts[0].setheading(90)

    def down(self):
        if self.total_parts[0].heading() != 90:
            self.total_parts[0].setheading(270)

    def right(self):
        if self.total_parts[0].heading() != 180:
            self.total_parts[0].setheading(0)

    def left(self):
        if self.total_parts[0].heading() != 0:
            self.total_parts[0].setheading(180)


# ----------CLASS TARGET--------------------
class Target(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("cyan")
        self.speed("fastest")
        self.eaten()

    def eaten(self):
        cond = True
        while cond:
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            if x % 20 == 0 and y % 20 == 0:  # align the food
                cond = False
        self.goto(x, y)


# -------------CLASS SCORE------------------------
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.point = 0
        self.color("white")
        self.goto(0, 310)
        self.write(f"Score: {self.point}", align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def add(self):
        self.clear()
        self.point += 1
        self.write(f"Score: {self.point}", align="center", font=("Courier", 20, "normal"))

    def end(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))


# ----------MAIN GAME WINDOW-----------------
window = Screen()
window.setup(width=640, height=700)
window.bgcolor("black")
window.title("Snake game")
window.tracer(0)
window.listen()
# Draw the outer frame manually
frame = turtle.Turtle()
frame.pencolor("white")
frame.pensize(1)
frame.speed("fastest")
frame.penup()
frame.goto(-310, 310)
frame.pendown()
frame.forward(620)
frame.setheading(270)
frame.forward(620)
frame.setheading(180)
frame.forward(620)
frame.setheading(90)
frame.forward(620)
frame.penup()
frame.hideturtle()

game = Body()  # start the game by creating the body
target = Target()
score = Score()


window.onkey(game.left, "Left")
window.onkey(game.right, "Right")
window.onkey(game.down, "Down")
window.onkey(game.up, "Up")
time.sleep(1)
game_cond = True
while game_cond:
    window.update()
    time.sleep(0.13)
    game.move()

    # eat
    if game.total_parts[0].distance(target) < 10:
        target.eaten()
        score.add()
        game.grow()

    # hit itself
    for part in game.total_parts[1:]:
        if game.total_parts[0].distance(part) < 10:
            score.end()
            game_cond = False
    # hit the wall
    if game.total_parts[0].ycor() > 300 or game.total_parts[0].ycor() < -300 or \
            game.total_parts[0].xcor() > 300 or game.total_parts[0].xcor() < -300:
        score.end()
        game_cond = False

del game
del score
del target
window.exitonclick()
