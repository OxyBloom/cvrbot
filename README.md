""
# CVRBot


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
sudo rosdep init
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
