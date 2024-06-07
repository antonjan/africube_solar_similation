import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cubesat(rotation_angle):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the vertices of the CubeSat
    vertices = np.array([
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
    ])

    # Define the edges of the CubeSat
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom face
        [4, 5], [5, 6], [6, 7], [7, 4],  # Top face
        [0, 4], [1, 5], [2, 6], [3, 7]   # Vertical edges
    ]

    # Rotate the CubeSat around the y-axis
    rotation_matrix = np.array([[np.cos(rotation_angle), 0, np.sin(rotation_angle)],
                                [0, 1, 0],
                                [-np.sin(rotation_angle), 0, np.cos(rotation_angle)]])
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Plot the CubeSat
    for edge in edges:
        ax.plot3D(rotated_vertices[edge, 0], rotated_vertices[edge, 1], rotated_vertices[edge, 2], 'b')

    # Set plot limits and labels
    ax.set_xlim([-1, 2])
    ax.set_ylim([-1, 2])
    ax.set_zlim([-1, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Set the number of frames and rotation speed
num_frames = 100
rotation_speed = 2 * np.pi / num_frames

# Generate the animation frames
for frame in range(num_frames):
    plot_cubesat(frame * rotation_speed)

