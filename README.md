# CVRBot
### Currently migrating to new gazebo. Expect Release Soon!
![cvr_bot_image v2](https://github.com/user-attachments/assets/54451a6c-dc5d-4ade-80e8-ca83ea193616)



# Setup
### Create a directory
```sh
mkdir ~/cvrbot_ws
cd ~/cvrbot_ws
```

### To Clone Repo-
```sh
git clone https://github.com/OxyBloom/cvrbot.git ./src/
```
### Get dependencies
```sh
rosdep update
cd ~/cvrbot_ws
rosdep install --from-paths src -y --ignore-src
```

### Build workspace
```sh
cd ~/cvrbot_ws
colcon build
```
### Source workspace

```sh
source install/setup.bash
```
### If you don't want to source workspace everytime add to your shell's configuration file for convenience, e.g., ~/.bashrc:

```sh
echo "source ~/cvrbot_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
# Adding Cameras Soon...

## :selfie: Media
[![YouTube](http://i.ytimg.com/vi/K5cwBx4CH-k/hqdefault.jpg)](https://www.youtube.com/watch?v=K5cwBx4CH-k)

[![YouTube](http://i.ytimg.com/vi/KDDOLi5bUGU/hqdefault.jpg)](https://www.youtube.com/watch?v=KDDOLi5bUGU)
