import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB1',
                'frame_id': 'laser',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )

        # Node(
        #     package="rplidar_ros",
        #     executable="rplidar_node",
        #     name="rplidar_node",
        #     parameters=[os.path.join(
        #         get_package_share_directory("cvr_bot_description"),
        #         "config",
        #         "rplidar_a1.yaml"
        #     )],
        #     output="screen"
        # )
    ])
