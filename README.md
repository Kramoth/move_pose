# Move Pose Package

This package contains the node `move_circle`, which publishes a `PoseStamped` message describing a circular trajectory.

---

## 🛠 Installation

To install this package, go to your ROS 2 workspace, or create one if it doesn't exist:

### Create a new workspace (if needed):
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```
### Clone the repository:
```bash
cd ~/ros2_ws/src
git clone https://github.com/Kramoth/move_pose.git
cd ~/ros2_ws
colcon build
```
---

## 🚀 Run the Node

In a first terminal:
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run move_pose move_circle
```
In a second terminal, launch RViz with the configuration file:
```bash
cd ~/ros2_ws
source install/setup.bash
rviz2 -d ~/ros2_ws/src/move_pose/config/default.rviz
```

---

## 🧾 Explanation

The node publishes `PoseStamped` messages, which are necessary for visualization in RViz.

You can view the structure of a `PoseStamped` message using:

ros2 interface show geometry_msgs/msg/PoseStamped 

A `PoseStamped` includes:
- A `header`, which defines the reference frame and the timestamp.
- A `pose`, composed of:
  - position (x, y, z)
  - orientation (as a quaternion: x, y, z, w)

---

## 📌 Reminder

RViz is a visualization tool, not a simulator. It allows you to graphically inspect the messages published on your ROS 2 topics in real time.
