#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class SerialAutoNode(Node):

    def __init__(self):
        super().__init__('serialauto_node')

        # ⚠️ chỉnh đúng cổng ESP32
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            self.get_logger().info("Serial connected!")
        except:
            self.get_logger().error("Cannot open serial port!")
            self.ser = None

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        self.get_logger().info("Node started, waiting for /cmd_vel...")

    def cmd_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z

        data = f"{linear:.2f},{angular:.2f}\n"

        if self.ser:
            self.ser.write(data.encode())

        self.get_logger().info(f"Send: {data.strip()}")

def main(args=None):
    rclpy.init(args=args)
    node = SerialAutoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
