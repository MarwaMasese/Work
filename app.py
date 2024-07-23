import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load 3D mesh object from an OBJ file
mesh = trimesh.load('/content/FinalBaseMesh.obj')

# Get the vertices and faces
vertices = mesh.vertices
faces = mesh.faces

# Function to render the 3D object from a specific angle
def render_object_at_angle(vertices, faces, angle, output_filename):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim([vertices[:, 0].min(), vertices[:, 0].max()])
    ax.set_ylim([vertices[:, 1].min(), vertices[:, 1].max()])
    ax.set_zlim([vertices[:, 2].min(), vertices[:, 2].max()])

    ax.view_init(elev=30, azim=angle)

    plt.savefig(output_filename)
    plt.close(fig)

# Render the 3D object at 12 different angles
def render_3d_object(vertices, faces, num_angles=12, output_prefix='output'):
    for i in range(num_angles):
        angle = i * (360 // num_angles)
        output_filename = f'{output_prefix}_{angle}.png'
        render_object_at_angle(vertices, faces, angle, output_filename)

# Render the 3D object
render_3d_object(vertices, faces)
