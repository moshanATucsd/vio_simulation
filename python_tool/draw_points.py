# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:18:24 2017

@author: hyj
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from GeometryLib import  drawCoordinateFrame, euler2Rbn,euler2Rnb
import transformations as tf

base_dir = '/Users/moshan/Documents/PhD/research/vio_simulation/bin'

point_id=[]
x=[]
y=[]
z=[]

with open(base_dir + '/all_points.txt', 'r') as f:
    data = f.readlines()  #txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data

    for line in data:
        odom = line.split()        #å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
        numbers_float = list(map(float, odom)) #è½¬åŒ–ä¸ºæµ®ç‚¹æ•°
        x.append( numbers_float[0] )
        y.append( numbers_float[1] )
        z.append( numbers_float[2] )


position = []
quaterntions = []
timestamp = []
qw_index = 1
with open(base_dir + '/cam_pose.txt', 'r') as f:   #   imu_circle   imu_spline

    data = f.readlines()  #txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data
    for line in data:
        odom = line.split()        #å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
        numbers_float = list(map(float, odom)) #è½¬åŒ–ä¸ºæµ®ç‚¹æ•°

        #timestamp.append( numbers_float[0])
        quaterntions.append( [numbers_float[qw_index], numbers_float[qw_index+1],numbers_float[qw_index+2],numbers_float[qw_index+3]   ] )   # qw,qx,qy,qz
        position.append( [numbers_float[qw_index+4], numbers_float[qw_index+5],numbers_float[qw_index+6] ] )


## plot 3d
fig = plt.figure()
plt.ion()
ax = fig.gca(projection='3d')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
rpy = []
t = []
for i in range(0,len(position),5):
    ax.clear()
    ax.scatter(x, y, z,c='g')

    x1=[]
    y1=[]
    z1=[]
    rpy.append( tf.euler_from_quaternion(quaterntions[i]) )
    t.append( position[i] )
    p = position[i]
    for j in range(len(rpy)):
        drawCoordinateFrame(ax, rpy[j], t[j])

    s = base_dir + '/keyframe/all_points_' +str(i)+'.txt'
    with open(s, 'r') as f:
        data = f.readlines()  #txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data
        for line in data:
            odom = line.split()        #å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
            numbers_float = list(map(float, odom)) #è½¬åŒ–ä¸ºæµ®ç‚¹æ•°
            x1.append( numbers_float[0] )
            y1.append( numbers_float[1] )
            z1.append( numbers_float[2] )

            plt.plot( [ numbers_float[0],   p[0]  ] , [ numbers_float[1], p[1] ] , zs=[ numbers_float[2], p[2] ])

    s = base_dir + '/models/car.txt'
    with open(s, 'r') as f:
        data = f.readlines()  # txtä¸­æ‰€æœ‰å­—ç¬¦ä¸²è¯»å…¥data
        for line in data:
            odom = line.split()  # å°†å•ä¸ªæ•°æ®åˆ†éš”å¼€å­˜å¥½
            numbers_float = list(map(float, odom))  # è½¬åŒ–ä¸ºæµ®ç‚¹æ•°
            plt.plot([numbers_float[0], numbers_float[3]], [numbers_float[1], numbers_float[4]],'b' ,zs=[numbers_float[2], numbers_float[5]])

    ax.scatter(x1, y1, z1,c='r',marker='^')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-15, 20)
    ax.set_ylim(-15, 20)
    ax.set_zlim(0, 20)
    # ax.legend()
    plt.show()
    plt.pause(1)