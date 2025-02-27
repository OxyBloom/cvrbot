import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    robot_description = ParameterValue(
        Command(
            [
                "xacro ",
                os.path.join(
                    get_package_share_directory("cvrbot_description"),
                    "urdf",
                    "robot.urdf.xacro",
                ),
                " is_sim:=False"
            ]
        ),
        value_type=str,
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}],
    )

    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[
            {"robot_description": robot_description,
             "use_sim_time": False},
            os.path.join(
                get_package_share_directory("bumperbot_controller"),
                "config",
                "bumperbot_controllers.yaml",
            ),
        ],
    )

    # imu_driver_node = Node(
    #     package="bumperbot_firmware",
    #     executable="mpu6050_driver.py"   bumperbot_utils
    # )
    
    imu_driver_node = Node(
        package="bumperbot_utils",
        executable="mpu6050_driver.py" 
    )

    imu_filtered = Node(
            package="imu_filter_madgwick",
            executable="imu_filter_madgwick_node",
            parameters=[{"publish_tf":False,"use_mag":False,"world_frame":"enu"}],
            remappings=[('imu/data_raw','imu/out'),('imu/data','imu')]
    )

    return LaunchDescription(
        [
            robot_state_publisher_node,
            controller_manager,
            imu_driver_node,
            imu_filtered
        ]
    )