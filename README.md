# In Progress...
```
We are currently trying to resolve the in accuracy of our odometry 
```
# CVRBot
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
