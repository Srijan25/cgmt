import matplotlib.pyplot as plt

def cohen_sutherland(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    # Compute the bit codes for the endpoints
    code1 = compute_bit_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_bit_code(x2, y2, x_min, y_min, x_max, y_max)

    # Initialize variables to indicate that both endpoints are inside the window
    inside1 = inside2 = True

    # Perform the Cohen-Sutherland algorithm
    while True:
        if not (code1 | code2):
            # Both endpoints are inside the window
            return x1, y1, x2, y2
        elif code1 & code2:
            # Both endpoints are outside the window, and they share a common region
            return None
        else:
            # Select an endpoint that is outside the window
            if not inside1:
                x1, y1 = bisection_method(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = bisection_method(x2, y2, x1, y1, x_min, y_min, x_max, y_max)
            
            # Update the bit code for the endpoint that was moved
            if inside1:
                code1 = compute_bit_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                code2 = compute_bit_code(x2, y2, x_min, y_min, x_max, y_max)
            
            # Update the variable indicating whether the endpoint is inside the window
            inside1 = not inside1


def compute_bit_code(x, y, x_min, y_min, x_max, y_max):
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


def bisection_method(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    # Compute the slope and y-intercept of the line
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    
    # Compute the x and y coordinates of the two midpoints
    xm = (x1 + x2) / 2
    ym = m * xm + b
    xm_left = x_min if xm < x_min else xm
    xm_right = x_max if xm > x_max else xm
    ym_left = m * xm_left + b
    ym_right = m * xm_right + b

    # Compute the bit codes for the midpoints
    code_left = compute_bit_code(xm_left, ym_left, x_min, y_min, x_max, y_max)
    code_right = compute_bit_code(xm_right, ym_right, x_min, y_min, x_max, y_max)

    # Use the midpoint that is inside the window
    if not code_left:
        return xm_left, ym_left
    elif not code_right:
        return xm_right, ym_right
    else:
        return None


# Define the clipping window
x_min, y_min, x_max, y_max = 0, 0, 10, 10

# Define the line to be clipped
x1, y1, x2, y2 = 3, 1, 7, 9

# Clip the line
clipped_line = cohen_sutherland(x1, y1, x2, y2, x_min, y_min, x_max, y_max)

# Plot the clipping window and the original line
fig, ax = plt.subplots()
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.plot([x1, x2], [y1, y2], label='Original Line')

# If the line was successfully clipped, plot the clipped line
if clipped_line:
    x1_c, y1_c, x2_c, y2_c = clipped_line
    ax.plot([x1_c, x2_c], [y1_c, y2_c], label='Clipped Line')

ax.legend()
plt.show()
