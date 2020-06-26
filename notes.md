## install

install sophus from github

```
mkdir build
cd build
cmake ..
make
```

create a folder named keyframe in bin folder
then ./data_gen in bin folder

## python 2 to 3

* map, follow [this](https://stackoverflow.com/questions/6800481/python-map-object-is-not-subscriptable)
* zip, follow [this](https://nelsonslog.wordpress.com/2015/04/20/python3-zip-is-a-hassle/)

## debug

* for random not in std error, follow [this](https://stackoverflow.com/questions/31790652/alternative-to-stddefault-random-engine-for-xcode), just `#include <random>`.

* for legend error, comment the ax.legend() line, since there is no legend to be plot

* has to run data_gen in the bin folder

## model

`10 10 6.5 0 10 6.5` means to connect `10 10 6.5` in xyz to `0 10 6.5` in xyz

## imu

* pose is in imu_pose, imu_int is the integration of pose to product trajectories

## cam imu

* what is t_bc, from body to cam?
* need to tune the sampling frequency

## extrinsic

```
cam.timestamp = imu.timestamp;
cam.Rwb = imu.Rwb * params.R_bc;    // cam frame in world frame
cam.twb = imu.twb + imu.Rwb * params.t_bc; //  Tcw = Twb * Tbc ,  t = Rwb * tbc + twb
```

```
// å¤–å‚æ•°
Eigen::Matrix3d R_bc;   // cam to body
Eigen::Vector3d t_bc;     // cam to body
```

Rwc = Rwb*Rbc
twc = Rwb*tbc + twb

tbc is pointing from b (imu) to camera !!

## save pose

cannot modify save pose function in imu.cpp, as it is also used by python code. Save imu data separately instead!

## total length

`len(position)` is the total length, not the default 400 
