from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


def plot_linear_cube(point_set, color='red'):
    fig = plt.figure()
    ax = Axes3D(fig)
    xx = point_set[:,0].reshape(-1).tolist()[0]
    yy = point_set[:,1].reshape(-1).tolist()[0]
    zz = point_set[:,2].reshape(-1).tolist()[0]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, zz, **kwargs)
    ax.plot3D([point_set[0,0], point_set[3,0]], [point_set[0,1], point_set[3,1]], [point_set[0,2], point_set[3,2]], **kwargs)
    ax.plot3D([point_set[4,0], point_set[7,0]], [point_set[4,1], point_set[7,1]], [point_set[4,2], point_set[7,2]], **kwargs)

    for i in range(4):
        ax.plot3D([point_set[i,0], point_set[i,0]], [point_set[i,1], point_set[i,1]], [point_set[i,2], point_set[4+i,2]], **kwargs)



    plt.title('Cube')
    plt.show()



