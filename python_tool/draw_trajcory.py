# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:18:24 2017

@author: hyj
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:43:55 2017

@author: hyj
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

base_dir = '/Users/moshan/Documents/PhD/research/vio_simulation/bin'

position = []
quaterntions = []
timestamp = []
tx_index = 5
with open(base_dir + '/imu_pose.txt', 'r') as f:  # imu_circle   imu_spline

    data = f.readlines()  # txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data
    for line in data:
        odom = line.split()  # å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
        numbers_float = list(map(float, odom))  # è½¬åŒ–ä¸ºæµ®ç‚¹æ•°

        position.append([numbers_float[tx_index], numbers_float[tx_index + 1], numbers_float[tx_index + 2]])

position1 = []
quaterntions1 = []
timestamp1 = []
with open(base_dir + '/imu_int_pose.txt', 'r') as f:  # imu_pose   imu_spline

    data = f.readlines()  # txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data
    for line in data:
        odom = line.split()  # å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
        numbers_float = list(map(float, odom))  # è½¬åŒ–ä¸ºæµ®ç‚¹æ•°

        # timestamp.append( numbers_float[0])
        # quaterntions1.append( [numbers_float[tx_index+6], numbers_float[tx_index+3],numbers_float[tx_index+4],numbers_float[tx_index+5]   ] )   # qw,qx,qy,qz
        position1.append([numbers_float[tx_index], numbers_float[tx_index + 1], numbers_float[tx_index + 2]])

position2 = []
quaterntions2 = []
timestamp2 = []
with open(base_dir + '/imu_int_pose_noise.txt', 'r') as f:  # cam_pose_opt_o_0   cam_pose_opt_o_0

    data = f.readlines()  # txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data
    for line in data:
        odom = line.split()  # å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
        numbers_float = list(map(float, odom))  # è½¬åŒ–ä¸ºæµ®ç‚¹æ•°

        # timestamp.append( numbers_float[0])
        # quaterntions2.append( [numbers_float[tx_index+6], numbers_float[tx_index+3],numbers_float[tx_index+4],numbers_float[tx_index+5]   ] )   # qw,qx,qy,qz
        position2.append([numbers_float[tx_index], numbers_float[tx_index + 1], numbers_float[tx_index + 2]])

    ### plot 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

xyz = list(zip(*position))
xyz1 = list(zip(*position1))
xyz2 = list(zip(*position2))
print
ax.plot(xyz[0], xyz[1], xyz[2], label='gt')
# ax.plot(xyz1[0], xyz1[1], xyz1[2], label='imu_int')
ax.plot(xyz2[0], xyz2[1], xyz2[2], label='noise')
ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
