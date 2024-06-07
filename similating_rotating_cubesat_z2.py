import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the CubeSat dimensions
length = 10  # cm
width = 10   # cm
height = 10  # cm

# Define the rotation parameters
rotation_speed = 0.1  # rad/s
rotation_axis = np.array([1, 1, 1])  # Rotation axis vector

# Generate the initial CubeSat vertices
vertices = np.array([
    [-length/2, -width/2, -height/2],  # Vertex 0
    [-length/2, width/2, -height/2],   # Vertex 1
    [length/2, width/2, -height/2],    # Vertex 2
    [length/2, -width/2, -height/2],   # Vertex 3
    [-length/2, -width/2, height/2],   # Vertex 4
    [-length/2, width/2, height/2],    # Vertex 5
    [length/2, width/2, height/2],     # Vertex 6
    [length/2, -width/2, height/2]     # Vertex 7
])

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the initial axis limits
ax.set_xlim([-length, length])
ax.set_ylim([-width, width])
ax.set_zlim([-height, height])

# Create a line collection to hold the edges of the CubeSat
lines = ax.plot([], [], [], 'k-')

# Animation update function
def update(frame):
    # Rotate the CubeSat vertices around the rotation axis
    angle = rotation_speed * frame
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Update the line collection data
    lines[0].set_data(rotated_vertices[[0, 1, 2, 3, 0], [0, 1, 2, 3, 0]].T[:2])
    lines[0].set_3d_properties(rotated_vertices[[0, 1, 2, 3, 0], 2])

    # Update the plot title with the current angle
    ax.set_title(f'Rotation Angle: {angle:.2f} rad')

    return lines

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Display the plot
plt.show()

