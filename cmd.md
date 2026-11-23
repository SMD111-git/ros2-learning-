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

