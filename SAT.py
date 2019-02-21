import numpy as np
import math

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


def collision_detect(ref_dimention, cuboid_corner):
    x_min = np.min(cuboid_corner[:, 0])
    x_max = np.max(cuboid_corner[:, 0])
    y_min = np.min(cuboid_corner[:, 1])
    y_max = np.max(cuboid_corner[:, 1])
    z_min = np.min(cuboid_corner[:, 2])
    z_max = np.max(cuboid_corner[:, 2])

    xref_min = -ref_dimention[0]/2
    xref_max = ref_dimention[0]/2
    yref_min = -ref_dimention[1]/2
    yref_max = ref_dimention[1]/2
    zref_min = -ref_dimention[2]/2
    zref_max = ref_dimention[2]/2

    x_collide = collide_check(xref_min, xref_max, x_min, x_max)
    y_collide = collide_check(yref_min, yref_max, y_min, y_max)
    z_collide = collide_check(zref_min, zref_max, z_min, z_max)



    return False

def InRef(cuboid_ref, cuboid):
    T_matrix = np.array([[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]])

    cuboid_corner_initial = np.array([cuboid["Dimention"][0]/2, cuboid["Dimention"][1]/2, cuboid["Dimention"][2]/2])
    cuboid_corner_dimension = np.tile(cuboid_corner_initial, (8,1))
    cuboid_corner = cuboid_corner_dimension * T_matrix
    Rotation_ref = RPY_to_Rotation(cuboid_ref["Orientation"])
    Rotation_cub = RPY_to_Rotation(cuboid["Orientation"])
    Rotation_cub_to_ref = Rotation_cub @ np.linalg.inv(Rotation_ref)
    cuboid_corner_after_Rotation = Rotation_cub_to_ref @ cuboid_corner.T

    cuboid_center_to_ref = cuboid["Origin"] - cuboid_ref["Origin"]
    cuboid_corner_new_axis = cuboid_corner_after_Rotation.T + np.tile(cuboid_center_to_ref, (8,1))
    Collision_or_not = collision_detect(cuboid_ref["Origin"],cuboid_corner_new_axis)
    return Collision_or_not



def collosion_detect(cuboid_1,cuboid_2):
    result1 = InRef(cuboid_1, cuboid_2)   #  In reference of cuboid1
    result2 = InRef(cuboid_2, cuboid_1)   #  In reference of cuboid2
    return (result1 or result2)


def main():
    cuboid_1 = {"Origin": [0, 0, 0], "Orientation": [0, 0, 0], "Dimension": [3, 1, 2]}
    cuboid_2 = {"Origin": [0, 0, 0], "Orientation": [0, 0, 0], "Dimension": [3, 1, 2]}
    print(collosion_detect(cuboid_1,cuboid_2))

if __name__ == '__main__':
    main();

