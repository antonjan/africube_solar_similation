import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def rotate_cube(theta):
    # Generate CubeSat coordinates
    cube_vertices = np.array([
        [1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1],
        [-1, 1, -1],
        [1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ])

    # Create rotation matrix
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Rotate CubeSat
    rotated_cube = np.dot(cube_vertices, rotation_matrix)

    return rotated_cube


# Generate CubeSat rotation over time
theta_values = np.linspace(0, 2 * np.pi, 100)
rotated_cubes = [rotate_cube(theta) for theta in theta_values]

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the rotated CubeSat at each time step
for rotated_cube in rotated_cubes:
    ax.cla()  # Clear previous plot
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.plot_trisurf(rotated_cube[:, 0], rotated_cube[:, 1], rotated_cube[:, 2])
    plt.pause(0.05)

plt.show()

