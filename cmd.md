1 :source /opt/ros/jazzy/setup.bash

mkdir -p ~/car5_learning_ws/src
cd ~/car5_learning_ws/src

ros2 pkg create --build-type ament_python \
  --dependencies rclpy nav_msgs \
  car5_learning

  or

ros2 pkg create car5_learning \
  --build-type ament_python \
  --dependencies rclpy nav_msgs



2-3 in code 


`` — Build only our new package``
4: cd ~/car5_learning_ws

source /opt/ros/jazzy/setup.bash

colcon build --packages-select car5_learning

source install/setup.bash



5:Run our monitor
ros2 run car5_learning odom_monitor

<img width="1265" height="485" alt="image" src="https://github.com/user-attachments/assets/53c1b5b5-895f-421f-b3d2-c4f6b3dfe172" />
<img width="875" height="592" alt="Screenshot 2026-11-23 145824" src="https://github.com/user-attachments/assets/6afcadcd-8c01-475d-818f-12ffbd7e7c2c" />


