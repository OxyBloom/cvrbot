import launch
import launch_ros
import os
import xacro

from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_prefix
from launch.actions import ExecuteProcess
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

pkg_name='cvr_bot_description'

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_models_dir = get_package_share_directory(pkg_name)

    install_dir = get_package_prefix(pkg_name)

    if 'GAZEBO_MODEL_PATH' in os.environ:
        gazebo_models_path = os.path.join(pkg_models_dir, 'meshes')
        os.environ['GAZEBO_MODEL_PATH'] = os.environ['GAZEBO_MODEL_PATH'] + ':' + gazebo_models_path
    else:
        os.environ['GAZEBO_MODEL_PATH'] =  install_dir + "/share"

    if 'GAZEBO_PLUGIN_PATH' in os.environ:
        os.environ['GAZEBO_PLUGIN_PATH'] = os.environ['GAZEBO_PLUGIN_PATH'] + ':' + install_dir + '/lib'
    else:
        os.environ['GAZEBO_PLUGIN_PATH'] = install_dir + '/lib'


    package_name='cvr_bot_description'

    # rsp = IncludeLaunchDescription(
    #             PythonLaunchDescriptionSource([os.path.join(
    #                 get_package_share_directory(package_name),'launch','rsp.launch.py'
    #             )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items()
    # )

    pkg_share = launch_ros.substitutions.FindPackageShare(package='cvr_bot_description').find('cvr_bot_description')

    # xacro_file_ebot = os.path.join(pkg_share, 'urdf/', 'cvr_bot_sim.xacro')
    # print(os.path.join(get_package_share_directory(pkg_name)))
    xacro_file_ebot = os.path.join(get_package_share_directory(pkg_name), 'urdf/', 'cvr_bot_sim.xacro')
    # xacro_file_ebot = os.path.join(get_package_share_directory('ebot_description'), 'models/', 'ebot/', 'ebot_description.xacro')
    assert os.path.exists(xacro_file_ebot), "The box_bot.xacro doesnt exist in "+str(xacro_file_ebot)
    robot_description_config_ebot = xacro.process_file(xacro_file_ebot)
    robot_description_bot = robot_description_config_ebot.toxml()

    robot_state_publisher_node_ebot = launch_ros.actions.Node(
        package='robot_state_publisher',
        name='cvr_bot',
        executable='robot_state_publisher',
        parameters=[{"robot_description": robot_description_bot}],
        remappings=[('robot_description', 'robot_description_cvrbot')]

    )

    static_transform = launch_ros.actions.Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_transform_publisher',
        arguments = ["0.0", "0.0", "0.0", "3.14", "0", "0", "world", "odom"],
        output='screen')

    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    twist_mux_params = os.path.join(get_package_share_directory(package_name),'config','twist_mux.yaml')
    twist_mux = Node(
            package="twist_mux",
            executable="twist_mux",
            parameters=[twist_mux_params, {'use_sim_time': True}],
            remappings=[('/cmd_vel_out','/diff_cont/cmd_vel_unstamped')]
        )

    gazebo_params_file = os.path.join(get_package_share_directory(package_name),'config','gazebo_params.yaml')

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                    # launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', name='bot_spawner', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description_cvrbot',
                                   '-entity', 'my_bot'],
                        output='screen')


    # diff_drive_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["diff_cont"],
    # )

    # joint_broad_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_broad"],
    # )


    # Code for delaying a node (I haven't tested how effective it is)
    # 
    # First add the below lines to imports
    # from launch.actions import RegisterEventHandler
    # from launch.event_handlers import OnProcessExit
    #
    # Then add the following below the current diff_drive_spawner
    # delayed_diff_drive_spawner = RegisterEventHandler(
    #     event_handler=OnProcessExit(
    #         target_action=spawn_entity,
    #         on_exit=[diff_drive_spawner],
    #     )
    # )
    #
    # Replace the diff_drive_spawner in the final return with delayed_diff_drive_spawner



    # Launch them all!
    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                            description='Flag to enable joint_state_publisher_gui'),
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='True',
                                            description='Flag to enable use_sim_time'),
        
        DeclareLaunchArgument(
            'world',
            default_value=[os.path.join(pkg_models_dir, 'worlds', 'obstacles.world'), ''],
        #   default_value=[os.path.join(pkg_models_dir, 'worlds', 'eyantra_warehouse_task0.world'), ''], # Change name of world file if required.
            description='SDF world file'),
        # rsp,
        gazebo,
        # ExecuteProcess(cmd=['gazebo', '--verbose', '-s','libgazebo_ros_init.so','libgazebo_ros_factory.so', 'libgazebo_ros_force_system.so'], output='screen'),
        robot_state_publisher_node_ebot,
        spawn_entity,
        # static_transform,
        joystick,
        twist_mux,
        # diff_drive_spawner,
        # joint_broad_spawner
    ])
