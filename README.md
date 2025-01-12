""
# CVRBot
![image](https://github.com/user-attachments/assets/a37533fa-4f4c-4799-baf4-0291fe242123)


# Setup
### Create a directory
```sh
mkdir ~/cvrbot_ws
cd ~/cvrbot_ws
```

### To Clone Repo-
```sh
git clone https://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@github.com/OxyBloom/cvrbot.git ./src/
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
