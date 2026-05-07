# Astra Mini S + RTABMAP + Nav2 (ROS2 Humble)

## Features
- Astra Mini S RGBD camera
- RTABMAP SLAM
- Nav2 navigation
- ESP32 motor control
- Teleop keyboard
- Depth to LaserScan

## Requirements
- Ubuntu 22.04
- ROS2 Humble

## Build

```bash
mkdir -p ~/astra_ws/src
cd ~/astra_ws/src

git clone <repo_link>

cd ~/astra_ws

source /opt/ros/humble/setup.bash

colcon build --symlink-install
```

## Run Camera

```bash
ros2 launch astra_camera astra.launch.xml
```

## Run RTABMAP

```bash
ros2 launch rtabmap_launch rtabmap.launch.py
```

## Navigation

```bash
ros2 launch nav2_bringup navigation_launch.py
```
