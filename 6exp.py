from tkinter import *

# function to clip a line segment using Cohen-Sutherland algorithm
def cohen_sutherland(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    # compute region codes for the endpoints of the line segment
    code1 = compute_region_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_region_code(x2, y2, x_min, y_min, x_max, y_max)
    
    # loop until the endpoints are inside the clipping window
    while True:
        # if both endpoints are inside the clipping window, we're done
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2
        
        # if the endpoints are in different regions, the line segment is outside the clipping window
        if code1 & code2 != 0:
            return None
        
        # pick an endpoint outside the clipping window
        code_out = code1 if code1 != 0 else code2
        x, y = None, None
        
        # find the intersection point of the line segment with the clipping window
        if code_out & 8:  # top
            x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            y = y_max
        elif code_out & 4:  # bottom
            x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            y = y_min
        elif code_out & 2:  # right
            y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            x = x_max
        elif code_out & 1:  # left
            y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            x = x_min
        
        # replace the outside endpoint with the intersection point and compute its region code
        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_region_code(x1, y1, x_min, y_min, x_max, y_max)
        else:
            x2, y2 = x, y
            code2 = compute_region_code(x2, y2, x_min, y_min, x_max, y_max)

# function to compute the region code of a point with respect to a clipping window
def compute_region_code(x, y, x_min, y_min, x_max, y_max):
    code = 0
    if x < x_min:
        code |= 1
    elif x > x_max:
        code |= 2
    if y < y_min:
        code |= 4
    elif y > y_max:
        code |= 8
    return code

# function to clip a line segment using the bisection method
def bisection_method(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    # compute the slope and y-intercept of the line segment
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    
    # clip the endpoints of the line segment using bisection method
    # clip the left endpoint
    if x1 < x_min:
        x1 = x_min
        y1 = m * x1 + b
    elif x1 > x_max:
        x1 = x_max
        y1 = m * x1 + b
    if y1 < y_min:
        y1 = y_min
        x1 = (y1 - b) / m
    elif y1 > y_max:
        y1 = y_max
        x1 = (y1 - b) / m
    
    # clip the right endpoint
    if x2 < x_min:
        x2 = x_min
        y2 = m * x2 + b
    elif x2 > x_max:
        x2 = x_max
        y2 = m * x2 + b
    if y2 < y_min:
        y2 = y_min
        x2 = (y2 - b) / m
    elif y2 > y_max:
        y2 = y_max
        x2 = (y2 - b) / m
    
    # return the clipped line segment
    return x1, y1, x2, y2
# create a Tkinter window and canvas
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

# draw the clipping window
canvas.create_rectangle(100, 100, 300, 300)

# draw the original line segment
x1, y1, x2, y2 = 50, 250, 350, 50
canvas.create_line(x1, y1, x2, y2, fill='blue')

# clip the line segment using Cohen-Sutherland algorithm and bisection method
x1, y1, x2, y2 = cohen_sutherland(x1, y1, x2, y2, 100, 100, 300, 300)
x1, y1, x2, y2 = bisection_method(x1, y1, x2, y2, 100, 100, 300, 300)

# draw the clipped line segment
canvas.create_line(x1, y1, x2, y2, fill='red')

# start the Tkinter event loop
root.mainloop()
