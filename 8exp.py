import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define 3D coordinates of a cube
X = np.array([0, 1, 1, 0, 0, 1, 1, 0])
Y = np.array([0, 0, 1, 1, 0, 0, 1, 1])
Z = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Plot the cube
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z)

# Translation transformation
tx, ty, tz = 1, 1, 1
T = np.array([[1, 0, 0, tx],
              [0, 1, 0, ty],
              [0, 0, 1, tz],
              [0, 0, 0, 1]])

# Apply translation transformation
X, Y, Z, _ = np.dot(T, np.vstack((X, Y, Z, np.ones(len(X)))))

# Plot the translated cube
ax.scatter(X, Y, Z)

# Scaling transformation
sx, sy, sz = 2, 2, 2
S = np.array([[sx, 0, 0, 0],
              [0, sy, 0, 0],
              [0, 0, sz, 0],
              [0, 0, 0, 1]])

# Apply scaling transformation
X, Y, Z, _ = np.dot(S, np.vstack((X, Y, Z, np.ones(len(X)))))

# Plot the scaled cube
ax.scatter(X, Y, Z)

# Rotation transformation
theta = np.pi/4
R = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
              [np.sin(theta), np.cos(theta), 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

# Apply rotation transformation
X, Y, Z, _ = np.dot(R, np.vstack((X, Y, Z, np.ones(len(X)))))

# Plot the rotated cube
ax.scatter(X, Y, Z)

# Set limits and labels
ax.set_xlim3d(-3, 3)
ax.set_ylim3d(-3, 3)
ax.set_zlim3d(-3, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
