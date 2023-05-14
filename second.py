import turtle

def drawCircle(xc, yc, r):
    x, y = 0, r
    d = 1 - r
    while x <= y:
        turtle.goto(xc + x, yc + y)
        turtle.goto(xc - x, yc + y)
        turtle.goto(xc + x, yc - y)
        turtle.goto(xc - x, yc - y)
        turtle.goto(xc + y, yc + x)
        turtle.goto(xc - y, yc + x)
        turtle.goto(xc + y, yc - x)
        turtle.goto(xc - y, yc - x)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

# Testing the function
drawCircle(0, 0, 100)
turtle.done()
import turtle

def drawCircle(x0, y0, radius):
    x = 0
    y = radius
    d = 3 - 2 * radius
    turtle.penup()
    turtle.goto(x0 + x, y0 + y)
    turtle.pendown()
    while y >= x:
        turtle.goto(x0 + x, y0 + y)
        turtle.goto(x0 + y, y0 + x)
        turtle.goto(x0 - y, y0 + x)
        turtle.goto(x0 - x, y0 + y)
        turtle.goto(x0 - x, y0 - y)
        turtle.goto(x0 - y, y0 - x)
        turtle.goto(x0 + y, y0 - x)
        turtle.goto(x0 + x, y0 - y)
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

# Testing the function
drawCircle(0, 0, 100)
turtle.done()


