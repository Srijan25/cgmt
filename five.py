import numpy as np
import matplotlib.pyplot as plt

# Define the shape to transform
x = np.array([0, 1, 1, 0])
y = np.array([0, 0, 1, 1])
shape = np.vstack((x, y, np.ones_like(x)))

# Translation matrix
def translate(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

# Scaling matrix
def scale(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

# Rotation matrix
def rotate(theta):
    cos = np.cos(theta)
    sin = np.sin(theta)
    return np.array([[cos, -sin, 0],
                     [sin, cos, 0],
                     [0, 0, 1]])

# Mirror reflection matrix along X axis
def mirror_x():
    return np.array([[-1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

# Mirror reflection matrix along Y axis
def mirror_y():
    return np.array([[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 1]])

# Shearing matrix
def shear(kx, ky):
    return np.array([[1, kx, 0],
                     [ky, 1, 0],
                     [0, 0, 1]])

# Test the functions
# Apply transformations to the shape
translation_matrix = translate(1, 2)
scaling_matrix = scale(2, 2)
rotation_matrix = rotate(np.pi/4)
mirror_x_matrix = mirror_x()
mirror_y_matrix = mirror_y()
shearing_matrix = shear(0.5, 0)

transformed_shape_1 = np.matmul(translation_matrix, shape)
transformed_shape_2 = np.matmul(rotation_matrix, shape)
transformed_shape_3 = np.matmul(mirror_x_matrix, shape)
transformed_shape_4 = np.matmul(mirror_y_matrix, shape)
transformed_shape_5 = np.matmul(scaling_matrix, shape)
transformed_shape_6 = np.matmul(shearing_matrix, shape)

# Plot the transformed shapes
fig, axs = plt.subplots(2, 3)

axs[0, 0].plot(shape[0,:], shape[1,:], color='blue', alpha=0.5)
axs[0, 0].plot(transformed_shape_1[0,:], transformed_shape_1[1,:], color='red', alpha=0.5)
axs[0, 0].set_title('Translation')

axs[0, 1].plot(shape[0,:], shape[1,:], color='blue', alpha=0.5)
axs[0, 1].plot(transformed_shape_2[0,:], transformed_shape_2[1,:], color='red', alpha=0.5)
axs[0, 1].set_title('Rotation')

axs[0, 2].plot(shape[0,:], shape[1,:], color='blue', alpha=0.5)
axs[0, 2].plot(transformed_shape_3[0,:], transformed_shape_3[1,:], color='red', alpha=0.5)
axs[0, 2].set_title('Mirror Reflection (X-axis)')

axs[1, 0].plot(shape[0,:], shape[1,:], color='blue', alpha=0.5)
axs[1, 0].plot(transformed_shape_4[0,:], transformed_shape_4[1,:], color='red', alpha=0.5)
axs[1, 0].set_title('Mirror Reflection (Y-axis)')

axs[1, 1].plot(shape[0,:], shape[1,:], color='blue', alpha=0.5)
axs[1, 1].plot(transformed_shape_5[0,:], transformed_shape_5[1,:], color='red', alpha=0.5)
axs[1, 1].set_title('Scaling')

axs[1, 2].plot(shape[0,:], shape[1,:], color='blue', alpha=0.5)
axs[1, 2].plot(transformed_shape_6[0,:], transformed_shape_6[1,:], color='red', alpha=0.5)
axs[1, 2].set_title('Shearing')

plt.tight_layout()
plt.show()