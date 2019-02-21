import numpy as np
import math

'''
    Transform the roll pitch yaw to rotation matrix
'''
def RPY_to_Rotation(roll, pitch, yaw):
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

def InRef(cuboid_ref, cuboid):
    T_matrix = np.ndarray([[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]])

    cuboid_corner = np.ndarray([[]])


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

