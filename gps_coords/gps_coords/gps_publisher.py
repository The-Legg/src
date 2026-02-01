import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class GpsPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(String, 'gps_coordinates', 10)
        self.timer = self.create_timer(1.0, self.publish_gps)
        self.get_logger().info('GPS Publisher started.')

    def publish_gps(self):
        latitude = 43.65 + random.uniform(-0.01, 0.01)
        longitude = -79.38 + random.uniform(-0.01, 0.01)
        msg = String()
        msg.data = f'lat: {latitude:.6f}, lon: {longitude:.6f}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = GpsPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()