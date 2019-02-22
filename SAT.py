import numpy as np
import math
from test import *




'''
    Transform the roll pitch yaw to rotation matrix
'''
def RPY_to_Rotation(RPY_list):
    roll, pitch, yaw = RPY_list[0], RPY_list[1], RPY_list[2]
    yawMatrix = np.matrix([
        [math.cos(yaw), -math.sin(yaw), 0],
        [math.sin(yaw), math.cos(yaw), 0],
        [0, 0, 1]
    ])

    pitchMatrix = np.matrix([
        [math.cos(pitch), 0, math.sin(pitch)],
        [0, 1, 0],
        [-math.sin(pitch), 0, math.cos(pitch)]
    ])

    rollMatrix = np.matrix([
        [1, 0, 0],
        [0, math.cos(roll), -math.sin(roll)],
        [0, math.sin(roll), math.cos(roll)]
    ])

    R = yawMatrix * pitchMatrix * rollMatrix
    return R

def collide_check(ref_min, ref_max, _min, _max):
    if ref_min>_max or ref_max<_min:
        return False
    return True

def collision_detect(ref_corner, cuboid_corner):
    x_min = np.min(cuboid_corner[:, 0])
    x_max = np.max(cuboid_corner[:, 0])
    y_min = np.min(cuboid_corner[:, 1])
    y_max = np.max(cuboid_corner[:, 1])
    z_min = np.min(cuboid_corner[:, 2])
    z_max = np.max(cuboid_corner[:, 2])

    xref_min = np.min(ref_corner[:, 0])
    xref_max = np.max(ref_corner[:, 0])
    yref_min = np.min(ref_corner[:, 1])
    yref_max = np.max(ref_corner[:, 1])
    zref_min = np.min(ref_corner[:, 2])
    zref_max = np.max(ref_corner[:, 2])
    # print(x_min, x_max, xref_min, xref_max)
    # print(y_min, y_max, yref_min, yref_max)
    # print(z_min, z_max, zref_min, zref_max)

    x_collide = collide_check(xref_min, xref_max, x_min, x_max)
    y_collide = collide_check(yref_min, yref_max, y_min, y_max)
    z_collide = collide_check(zref_min, zref_max, z_min, z_max)

    return (x_collide and y_collide and z_collide)

def InRef(cuboid_ref, cuboid):
    T_matrix = np.array([[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1]])
    Projection_matrix = np.array([[1,0,0],[0,1,0],[0,0,1]])

    Rotation_ref = RPY_to_Rotation(cuboid_ref["Orientation"])
    Rotation_cub = RPY_to_Rotation(cuboid["Orientation"])

    cuboid_corner_initial = np.array(
        [cuboid["Dimension"][0] / 2, cuboid["Dimension"][1] / 2, cuboid["Dimension"][2] / 2])
    cuboid_corner_dimension = np.tile(cuboid_corner_initial, (8, 1))
    cuboid_corner = cuboid_corner_dimension * T_matrix

    ref_corner_initial = np.array(
        [cuboid_ref["Dimension"][0] / 2, cuboid_ref["Dimension"][1] / 2, cuboid_ref["Dimension"][2] / 2])
    ref_corner_dimension = np.tile(ref_corner_initial, (8, 1))
    ref_corner = ref_corner_dimension * T_matrix

    ref_corners = ref_corner @ Rotation_ref + np.array(cuboid_ref["Origin"])
    cub_corners = cuboid_corner @ Rotation_cub + np.array(cuboid["Origin"])
    # plot_linear_cube(cub_corners, ref_corners, color='red')

    Projection_matrix_ref = Projection_matrix @ Rotation_ref
    cuboid_corner_new = cub_corners @ Projection_matrix_ref.T
    ref_corner_new = ref_corners @ Projection_matrix_ref.T
    # plot_linear_cube(cuboid_corner_new, ref_corner_new, color='red')

    Collision_or_not_ref = collision_detect(ref_corner_new,cuboid_corner_new)

    Projection_matrix_cub = Projection_matrix @ Rotation_cub
    cuboid_corner_new = cub_corners @ Projection_matrix_cub.T
    ref_corner_new = ref_corners @ Projection_matrix_cub.T

    Collision_or_not_cub = collision_detect(ref_corner_new,cuboid_corner_new)


    return Collision_or_not_ref and Collision_or_not_cub


def collosion_detect(cuboid_1,cuboid_2):
    result1 = InRef(cuboid_1, cuboid_2)   #  In reference of cuboid1
    return result1


def main():
    cuboid_1 = {"Origin": [0, 0, 0], "Orientation": [0, 0, 0], "Dimension": [2, 2, 2]}
    cuboid_2 = {"Origin": [1.7, 1.7, 0], "Orientation": [0, 0, np.pi/4], "Dimension": [2, 2, 2]}
    print(collosion_detect(cuboid_1,cuboid_2))

if __name__ == '__main__':
    main();

