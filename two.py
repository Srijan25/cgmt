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
