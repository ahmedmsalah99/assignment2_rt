# Assignment 2

This project is divided into two parts, each with different ROS versions. The first part uses ROS Melodic, while the second part uses ROS2 Humble with colcon build (neotic and foxy are ok too).

## Part 1: ROS

This part of the project is built with ROS.

### Steps for building

1. Run the following command to build the project:
    ```bash
    catkin_make
    ```

2. If you don’t have the models installed, set the `GAZEBO_MODEL_PATH` to the folder in the repo:
    ```bash
    export GAZEBO_MODEL_PATH=<path_to_repo>/models
    ```

### Running the simulation

1. Source the setup file:
    ```bash
    source devel/setup.bash
    ```

2. Launch the simulation:
    ```bash
    roslaunch assignment_2_2024 assignment1.launch
    ```

### Commands and Topics

- To send a goal, publish on the following topics (you can use "rostopic pub"):
    - `set_goal` (Pose)
    - `cancel_goal` (No data)

- To retrieve the last sent goal, use the service:
    ```bash
    rosservice call /get_goal
    ```

---

## Part 2: ROS2

This part of the project is built with ROS2 using colcon build.

### Steps for building

1. Build the project using colcon:
    ```bash
    colcon build
    ```

2. Source the setup file:
    ```bash
    source install/setup.sh
    ```

### Launch the simulation

1. Launch the simulation with the following command:
    ```bash
    ros2 launch robot_urdf gazebo.launch.py
    ```

2. In another terminal, run the UI:
    ```bash
    ros2 run robot_urdf UI
    ```

### Commands

You can enter your commands in the terminal after running the UI.
