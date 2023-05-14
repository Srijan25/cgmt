import turtle

# create turtle object
t = turtle.Turtle()

# set the speed of the turtle
t.speed(0)

# set the pen color
t.pencolor('black')

# set the fill color
t.fillcolor('red')

# define the vertices of the polygon
vertices = [(0, 0), (100, 0), (100, 100), (50, 150), (0, 100)]

# draw the polygon
t.penup()
t.goto(vertices[0])
t.pendown()
t.begin_fill()
for v in vertices:
    t.goto(v)
t.end_fill()

# flood fill algorithm
def flood_fill(x, y, fill_color, boundary_color):
    if t.pencolor() != boundary_color and t.fillcolor() != fill_color:
        t.begin_fill()
        t.forward(1)
        t.left(90)
        t.forward(1)
        t.right(90)
        t.end_fill()
        flood_fill(x+1, y, fill_color, boundary_color)
        flood_fill(x-1, y, fill_color, boundary_color)
        flood_fill(x, y+1, fill_color, boundary_color)
        flood_fill(x, y-1, fill_color, boundary_color)

# call the flood fill algorithm
flood_fill(50, 50, 'green', 'black')

# boundary fill algorithm
def boundary_fill(x, y, fill_color, boundary_color):
    if t.pencolor() != boundary_color and t.fillcolor() != fill_color:
        t.fillcolor(fill_color)
        t.forward(1)
        t.left(90)
        t.forward(1)
        t.right(90)
        boundary_fill(x+1, y, fill_color, boundary_color)
        boundary_fill(x-1, y, fill_color, boundary_color)
        boundary_fill(x, y+1, fill_color, boundary_color)
        boundary_fill(x, y-1, fill_color, boundary_color)

# call the boundary fill algorithm
boundary_fill(50, 50, 'blue', 'black')

# scan-line algorithm
def scan_line(x1, y1, x2, y2, fill_color):
    t.pencolor(fill_color)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.begin_fill()
    for i in range(y1, y2+1):
        t.goto(x1, i)
        t.goto(x2, i)
    t.end_fill()

# call the scan-line algorithm
scan_line(0, 0, 100, 100, 'yellow')

# hide the turtle
t.hideturtle()

# update the screen
turtle.done()