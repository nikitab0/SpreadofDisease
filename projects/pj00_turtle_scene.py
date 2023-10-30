"""A mountain landscape will be drawn using Turtle."""
from turtle import Turtle, colormode, done
colormode(255)

__author__ = "730393935"


def main() -> None:
    """The entrypoint of my scene."""
    sam_turtle: Turtle = Turtle()
    sam_turtle.color(78, 115, 158)
    draw_rec(sam_turtle, -950, -650, 1300, 1900)
    sam_turtle.color(250, 250, 250)
    draw_circle(sam_turtle, 0, 20, 75)
    sam_turtle.color(178, 62, 85)
    draw_tri(sam_turtle, -250, -250, 400)
    draw_tri(sam_turtle, -200, -250, 370)
    draw_tri(sam_turtle, -90, -250, 370)
    sam_turtle.color(155, 52, 75)
    draw_tri(sam_turtle, -950, -750, 1200)
    draw_tri(sam_turtle, -1100, -750, 1000)
    draw_tri(sam_turtle, 0, -650, 1000)
    draw_tri(sam_turtle, 0, -500, 900)
    sam_turtle.color(98, 50, 78)
    draw_mtn(sam_turtle, -1100, -650, 800, 3)
    draw_mtn(sam_turtle, -400, -650, 700, 2)
    draw_mtn(sam_turtle, 50, -650, 800, 3)
    sam_turtle.color(79, 57, 97)
    draw_mtn(sam_turtle, -1100, -650, 650, 4)
    draw_mtn(sam_turtle, -1120, -650, 620, 4)
    draw_mtn(sam_turtle, -400, -650, 600, 3)
    draw_mtn(sam_turtle, 50, -650, 650, 3)
    draw_mtn(sam_turtle, 30, -650, 630, 3)
    sam_turtle.color(49, 24, 97)
    draw_mtn(sam_turtle, -1000, -550, 350, 10)
    sam_turtle.color(29, 8, 70)
    draw_rec(sam_turtle, -720, -400, 40, 2000)
    draw_circle(sam_turtle, -500, -1400, 570)
    draw_tree(sam_turtle, -500, -350, 20, 250, 25)
    draw_tree(sam_turtle, -720, -300, 15, 200, 20)
    draw_circle(sam_turtle, 400, -1400, 570)
    draw_tree(sam_turtle, 450, -350, 20, 300, 30)
    draw_grass(sam_turtle, -190, -360, 15, 95)
    draw_circle(sam_turtle, 170, -300, 15)
    draw_circle(sam_turtle, 190, -290, 23)
    draw_bird(sam_turtle, 0, 100, 1)
    draw_bird(sam_turtle, 15, 120, 1)
    draw_bird(sam_turtle, 55, 160, 1)
    draw_bird(sam_turtle, -9, 140, 1)
    draw_bird(sam_turtle, 70, 200, 1)
    draw_bird(sam_turtle, 85, 160, 1)
    done()


def draw_sq(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws and fills a square."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        a_turtle.forward(width)
        a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.penup()


def draw_rec(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None: 
    """Draws and fills a rectangle."""
    a_turtle.speed(50)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while (i < 2):
        a_turtle.forward(length)
        a_turtle.left(90)
        a_turtle.forward(width)
        a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.penup()


def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws and fills a circle."""
    a_turtle.speed(50)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_tri(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draws and fills a triangle."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while (i < 3):
        a_turtle.forward(side_length)
        a_turtle.left(120)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.penup()


def draw_mtn(a_turtle: Turtle, x: float, y: float, side_length: float, peaks: int) -> None:
    """Draws a mountain range."""
    i: int = 0
    while (i < peaks):
        draw_tri(a_turtle, x, y, side_length)
        x = x + 170
        i = i + 1


def draw_tree(a_turtle: Turtle, x: float, y: float, width: float, length: float, branchs: int) -> None:
    """Draws and fills a tree."""
    i: int = 0
    while (i < branchs):
        draw_rec(a_turtle, x, y, width, length)
        x = x + 5
        y = y + width
        length = length - 10
        i = i + 1


def draw_line(a_turtle: Turtle, x: float, y: float, length: float) -> None: 
    """Draws a verticle line."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.forward(length)
    a_turtle.penup()


def draw_grass(a_turtle: Turtle, x: float, y: float, length: float, blades: int) -> None:
    """Draws grass."""
    i: int = 0
    a_turtle.left(90)
    while (i < blades):
        draw_line(a_turtle, x, y, length)
        x = x + 3
        i = i + 1


def draw_bird(a_turtle: Turtle, x: float, y: float, side_length: int) -> None:
    """Draws a bird with either wings up or down."""
    a_turtle.color(0, 0, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    i: int = 0
    a_turtle.left(90)
    while (i < 18):
        a_turtle.forward(side_length)
        a_turtle.left(5)
        i = i + 1
    a_turtle.left(180)
    h: int = 0
    while (h < 18):
        a_turtle.forward(side_length)
        a_turtle.left(5)
        h = h + 1
    a_turtle.left(90)
    a_turtle.penup()
    a_turtle.hideturtle()


if __name__ == "__main__":
    main()