import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Helper function to create a Bezier curve
def create_bezier(control_points, num_points):
    t = np.linspace(0, 1, num_points)
    n = len(control_points)
    curve = np.zeros((num_points, 2))
    for i in range(n):
        curve += np.outer((1 - t) ** (n - i - 1) * t ** i, control_points[i])
    return curve

# Define control points for the curve
control_points = np.array([[0, 0], [1, 3], [3, 4], [5, 2], [6, 1]])

# Reshape control points for B-spline
x = np.arange(len(control_points))
y = control_points.T
t = np.linspace(0, len(control_points) - 1, 100)

# Generate B-spline curve
spl = make_interp_spline(x, y.T, k=3)  # Transpose y
bspline_curve = np.array(spl(t)).T

# Generate Bezier curve
bezier_curve = create_bezier(control_points, 100)

# Plot the curves
plt.plot(control_points[:, 0], control_points[:, 1], 'o', label='Control Points')
plt.plot(bspline_curve[:, 0], bspline_curve[:, 1], label='B-Spline Curve')
plt.plot(bezier_curve[:, 0], bezier_curve[:, 1], label='Bezier Curve')
plt.legend()
plt.show()
