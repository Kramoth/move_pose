# move_pose

## Installation
Pour installer ce package, dans le dossier source de votre catkin workspace faire un clone du package:
On supposera que votre catkin workspace s'appelle catkin_ws et se situe dans votre home, remplacer par le bon chemin suivant l'oragnisation de vos dossiers.

```sh
cd catkin_ws/src
git clone https://www.github.com/kramoth/move_pose.git
```

Puis compiler et sourcer le setup.bash
```sh
catkin build
source ~/catkin_ws/devel/setup.bash
```

## Utilisation 
### circle pose
#### Avec rosrun

Dans un premier terminal lancer le serveur ROS
```sh
roscore
```

Dans un second terminal 
```sh
source ~/catkin_ws/devel/setup.bash
rosrun move_pose circle_pose.py
```

Dans un troisieme terminal
```sh
source ~/catkin_ws/devel/setup.bash
rosrun move_pose subscriber.py /subscribed_topic:=/published_topic
```
Pour visualiser, dans un autre terminal 
```sh
source ~/catkin_ws/devel/setup.bash
rosrun rviz rviz -d `rospack find move_pose`/rviz/circle_visualization.rviz
```

#### Avec roslaunch

Dans un terminal
```sh
roslaunch move_pose circle.launch
```
### teleop move
#### Avec rosrun
Dans un premier terminal lancer le serveur ROS
```sh
roscore
```
Pour installer le package teleop_twist_keyboard:
```sh
sudo apt-get install ros-noetic-teleop-twist-keyboard
```
Dans un second terminal lancer le noeud suivant:
```sh
rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
```
Dans un troisieme terminal
```sh
source ~/catkin_ws/devel/setup.bash
rosrun move_pose teleop_pose.py
```
Lancer rviz pour pour visualiser le pose stamped:
```sh
source ~/catkin_ws/devel/setup.bash
rosrun rviz rviz -d `rospack find move_pose`/rviz/teleop_visualization.rviz
```
#### Avec roslaunch
Dans un terminal:
```sh
source ~/catkin_ws/devel/setup.bash
roslaunch move_pose teleop.launch
```
