cmake_minimum_required(VERSION 3.8)
project(cvrbot_firmware)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(hardware_interface REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(PkgConfig)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(twist_mux_msgs REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(visualization_msgs REQUIRED)
pkg_check_modules(SERIAL libserial)

add_executable(safety_stop src/safety_stop.cpp)
ament_target_dependencies(safety_stop rclcpp std_msgs sensor_msgs geometry_msgs twist_mux_msgs rclcpp_action visualization_msgs)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  ${PROJECT_NAME}/mpu6050_driver.py
  ${PROJECT_NAME}/safety_stop.py
  DESTINATION lib/${PROJECT_NAME}
)

install(TARGETS
  safety_stop
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
)

ament_package()
