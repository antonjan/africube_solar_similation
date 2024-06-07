import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh

# Load the STL file
stl_file = mesh.Mesh.from_file('/home/anton/africube_frame/STL_Files/CubeSat_Solarpanel_Wing.STL')

# Extract vertices
vertices = stl_file.vectors.reshape(-1, 3)

# Create 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')

# Plot the vertices
ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

# Rotate the plot
for angle in range(0, 360):
    ax.view_init(azim=angle)
    plt.draw()
    plt.pause(0.001)

plt.show()

