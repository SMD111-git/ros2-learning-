cd ~/car5_learning_ws/src/car5_learning
nano car5_learning/odom_monitor.py
    
import math
import time

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class Car5OdomMonitor(Node):

    def __init__(self):
        super().__init__('car5_odom_monitor')

        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.last_display_time = 0.0

        self.get_logger().info(
            'Car-5 odometry monitor started'
        )

    def odom_callback(self, msg):

        # Read robot position
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # Read orientation quaternion
        q = msg.pose.pose.orientation

        # Convert quaternion into yaw angle
        sin_yaw = 2.0 * (q.w * q.z + q.x * q.y)
        cos_yaw = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)

        yaw = math.atan2(sin_yaw, cos_yaw)

        # Convert radians into degrees
        yaw_degrees = math.degrees(yaw)

        # Read robot velocity
        linear_speed = msg.twist.twist.linear.x
        angular_speed = msg.twist.twist.angular.z

        # Display once per second
        now = time.monotonic()

        if now - self.last_display_time >= 1.0:

            self.get_logger().info(
                f'X: {x:.3f} m | '
                f'Y: {y:.3f} m | '
                f'Heading: {yaw_degrees:.1f} deg | '
                f'Linear: {linear_speed:.3f} m/s | '
                f'Angular: {angular_speed:.3f} rad/s'
            )

            self.last_display_time = now


def main(args=None):

    rclpy.init(args=args)

    node = Car5OdomMonitor()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

