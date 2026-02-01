import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GpsSubscriber(Node):
    def __init__(self):
        super().__init__('gps_subscriber')
        self.subscription = self.create_subscription(
            String,
            'gps_coordinates',
            self.listener_callback,
            10)
        self.get_logger().info('GPS Subscriber started.')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = GpsSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()