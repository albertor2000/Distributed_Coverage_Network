# Distributed_Coverage_Network

## Description

A service for ROS2 to explore a map using LLoyd algorithm with Vornoi regions, to equally distribute the area between a discrete number of agents.

## Requirements

- Ubuntu Linux
- ROS Foxy

## Running

1. First of all, building your workspace with
```
colcon build
```
2. Open 4 more terminals
3. Source the project in each terminal using
```
source install/setup.bash
```
4. Navigate into launch file and run in the first terminal the following commands
```
cd robots_control/launch
ros2 launch start0.launch.py
```
5. In the second terminal, navigate into the second launch file and run the following commands
```
cd robots_control/launch
ros2 launch start1.launch.py
```
6. Once all is ready, in the third terminal, run the control node with
```
ros2 run robots_control control
```
7. Finally, in the fourth and fifth terminal, run respectively this two commands:
```
ros2 run agents_pos_service twin0 # In the first terminal
```
```
ros2 run agents_pos_service twin1 # In the second terminal
```

## Contributors

[albertor2000](https://github.com/albertor2000)
