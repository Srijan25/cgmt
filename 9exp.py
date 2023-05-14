import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d

# Define x and y values for the original curve
x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)

# Interpolate the curve using cubic spline
cs = CubicSpline(x, y)

# Interpolate the curve using linear interpolation
f = interp1d(x, y, kind='linear')

# Define x values for the interpolated curves
x_new = np.linspace(0, 2*np.pi, 100)

# Evaluate the interpolated curves at x_new values
y_cs = cs(x_new)
y_f = f(x_new)

# Plot the original curve and the interpolated curves
fig, ax = plt.subplots()
ax.plot(x, y, 'o', label='Original Curve')
ax.plot(x_new, y_cs, label='Cubic Spline Interpolation')
ax.plot(x_new, y_f, label='Linear Interpolation')
ax.legend()

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Interpolated Curves')

# Show the plot
plt.show()
