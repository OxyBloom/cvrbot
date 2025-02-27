import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # use_slam = LaunchConfiguration("use_slam")

    # use_slam_arg = DeclareLaunchArgument(
    #     "use_slam",
    #     default_value="false"
    # )

    hardware_interface = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("bumperbot_firmware"),
            "launch",
            "hardware_interface.launch.py"
        ),
    )

    # laser_driver = Node(
    #         package="rplidar_ros",
    #         executable="rplidar_node",
    #         name="rplidar_node",
    #         parameters=[os.path.join(
    #             get_package_share_directory("bumperbot_bringup"),
    #             "config",
    #             "rplidar_a1.yaml"
    #         )],
    #         output="screen"
    # )

    laser_interface = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                FindPackageShare("rplidar_ros").find("rplidar_ros"),
                "launch",
                "rplidar_a1_launch.py"
            )
        ),
        launch_arguments={
            "serial_port": "/dev/ttyUSB0",
            "frame_id": "laser_link",
            "inverted": "true",
            "angle_compensate": "true",
            "scan_mode": "Standard"
        }.items(),
    )
    

    # laser_driver = Node(
    #         package='rplidar_ros',
    #         executable='rplidar_composition',
    #         output='screen',
    #         # parameters=[os.path.join(
    #         #     get_package_share_directory("bumperbot_bringup"),
    #         #     "config",
    #         #     "rplidar_a1.yaml"
    #         # )],
    #         parameters=[{
    #             'serial_port': '/dev/ttyUSB0',
    #             'frame_id': 'laser',
    #             'inverted': False,
    #             'angle_compensate': True,
    #             'scan_mode': 'Standard'
    #         }]
    # )
    
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("bumperbot_controller"),
            "launch",
            "controller.launch.py"
        ),
        launch_arguments={
            "use_simple_controller": "False",
            "use_python": "False"
        }.items(),
    )
    
    joystick = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("bumperbot_controller"),
            "launch",
            "joystick_teleop.launch.py"
        ),
    )

    safety_stop = Node(
        package="bumperbot_utils",
        executable="safety_stop",
        output="screen",
    )

    
    return LaunchDescription([
        hardware_interface,
        # laser_driver,
        laser_interface,
        controller,
        joystick,
        # safety_stop,
    ])