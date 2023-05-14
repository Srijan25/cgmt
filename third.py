import turtle

def drawEllipse(xc, yc, a, b):
    x = 0
    y = b
    d1 = b * b - a * a * b + 0.25 * a * a
    dx = 2 * b * b * x
    dy = 2 * a * a * y

    while dx < dy:
        turtle.goto(xc + x, yc + y)
        turtle.goto(xc - x, yc + y)
        turtle.goto(xc + x, yc - y)
        turtle.goto(xc - x, yc - y)
        x += 1
        dx += 2 * b * b
        if d1 < 0:
            d1 += dx + b * b
        else:
            y -= 1
            dy -= 2 * a * a
            d1 += dx - dy + b * b

    d2 = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
    while y >= 0:
        turtle.goto(xc + x, yc + y)
        turtle.goto(xc - x, yc + y)
        turtle.goto(xc + x, yc - y)
        turtle.goto(xc - x, yc - y)
        y -= 1
        if d2 > 0:
            d2 -= dy - a * a
        else:
            x += 1
            dx += 2 * b * b
            d2 += dx - dy + a * a
            

# Testing the function
drawEllipse(0, 0, 100, 50)
turtle.done()


