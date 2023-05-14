import matplotlib.pyplot as plt

def generate_line(x1, y1, x2, y2):
  # Calculate slope (m)
  if x2 - x1 == 0:
    m = None # Slope is undefined for vertical lines
  else:
    m = (y2 - y1) / (x2 - x1)
  
  # Calculate the y-intercept (b)
  b = y1 - (m * x1)
  
  return m, b

# Define two points on the line
x1, y1, x2, y2 = 1, 1, 4, 4

# Generate the line using the slope method
m, b = generate_line(x1, y1, x2, y2)

# Plot the line
x = [x1, x2]
if m is None:
  # Line is vertical, x is constant
  y = [y1, y1]
else:
  y = [m*xx + b for xx in x]
  
plt.plot(x, y, '-r', label='Line')
plt.legend(loc='best')
plt.show()




import matplotlib.pyplot as plt

def generate_line_dda(x1, y1, x2, y2):
  # Calculate the differences between the points
  dx = x2 - x1
  dy = y2 - y1
  
  # Calculate the number of steps
  steps = max(abs(dx), abs(dy))
  
  # Calculate the increment in x and y for each step
  x_inc = dx / steps
  y_inc = dy / steps
  
  # Initialize the start point
  x, y = x1, y1
  
  # Store the points in a list
  points = []
  for i in range(steps + 1):
    points.append((round(x), round(y)))
    x += x_inc
    y += y_inc
  
  return points

# Define two points on the line
x1, y1, x2, y2 = 1, 1, 4, 4

# Generate the line using the DDA algorithm
points = generate_line_dda(x1, y1, x2, y2)
# Plot the line
x, y = zip(*points)
plt.plot(x, y, '-r', label='Line')
plt.legend(loc='best')
plt.show()





import matplotlib.pyplot as plt

def generate_line_bresenham(x1, y1, x2, y2):
  # Calculate the differences between the points
  dx = x2 - x1
  dy = y2 - y1
  
  # Determine the direction of the line
  if dx < 0:
    dx = -dx
    x_step = -1
  else:
    x_step = 1
    
  if dy < 0:
    dy = -dy
    y_step = -1
  else:
    y_step = 1
  
  # Initialize the starting point
  x, y = x1, y1
  
# Store the points in a list
  points = []
  if dx > dy:
    two_dy = 2 * dy
    two_dy_dx = 2 * (dy - dx)
    error = 2 * dy - dx
    for i in range(dx):
      points.append((x, y))
      if error >= 0:
        y += y_step
        error += two_dy_dx
      else:
        error += two_dy
      x += x_step
  else:
    two_dx = 2 * dx
    two_dx_dy = 2 * (dx - dy)
    error = 2 * dx - dy
    for i in range(dy):
      points.append((x, y))
      if error >= 0:
        x += x_step
        error += two_dx_dy
      else:
        error += two_dx
      y += y_step

    return points

# Define two points on the line
x1, y1, x2, y2 = 1, 1, 4, 4

# Generate the line using the Bresenham's algorithm
points = generate_line_bresenham(x1, y1, x2, y2)

# Plot the line
x, y = zip(*points)
plt.plot(x, y, '-r', label='Line')
plt.legend(loc='best')
plt.show()

