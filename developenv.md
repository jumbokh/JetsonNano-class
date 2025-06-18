### 安裝開發環境
* python --version
* python3 --version
* sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol
* sudo apt-get install python-rpi.gpio python3-rpi.gpio
* sudo apt install python3-opencv
* mkdir src
* ### 3. 設定 python3 為 default python [參考](https://linuxconfig.org/change-default-python-version-on-raspbian-gnu-linuxl)
* Step 1. Add both (all) versions of python installed to the list of "alternatives" for the python binary.
<pre>
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
</pre>
* Step 2. Select desired version:
<pre>
sudo update-alternatives --config python
</pre>
### 4. 設定 virtual env, and install packages
* 參考: [Donkey Car 環境設定](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%B8%80%E3%80%81Raspberry_Pi%E5%AE%89%E8%A3%85)
#### 相關軟體安裝 ( 參考: [Install OpenCV 4 on Raspberry Pi 4 and Raspbian Buster](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) )
<pre>
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python3-dev python3-pip python3-virtualenv python3-numpy python3-libcamera  -y
sudo apt-get install python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran  -y
sudo apt-get install libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp -y
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev   -y
sudo apt-get install libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev -y ### libqtgui4 libqt4-test  -y
sudo apt-get install cmake pkg-config libjpeg-dev libpng-dev libavcodec-dev libavformat-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev -y
sudo apt-get install libgtk2.0-dev libgtk-3-dev libatlas-base-dev -y
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103 -y
sudo apt-get install libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 -y
</pre>
##
#### install pip
<pre>
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo python3 get-pip.py
$ sudo rm -rf ~/.cache/pip
</pre>
##
#### install tensorflow 2.x
* [TensorFlow 2 on Raspberry Pi](https://towardsdatascience.com/3-ways-to-install-tensorflow-2-on-raspberry-pi-fe1fa2da9104)
* [3 Ways to Install TensorFlow 2 on Raspberry Pi](bitsy.ai/3-ways-to-install-tensorflow-on-raspberry-pi)
* [Community-built TensorFlow binaries](https://github.com/bitsy-ai/tensorflow-arm-bin)
#### 遠端桌面連線
* sudo apt-get install xrdp
* 在 win10 上執行遠端桌面連線 (可以調整選項, 以免佔用全部螢幕)
#### 新建虛擬環境 env
<pre>
pip3 install virtualenv
python3 -m virtualenv -p python3 env --system-site-packages
echo "source ~/env/bin/activate" >> ~/.bashrc
source ~/.bashrc
deactivate # 離開虛擬環境
</pre>
##
<pre>
python3 -m venv ds python=3.9
source ds/bin/activate
pip list
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn scipy sklearn imageio 
pip install jupyter notebook
pip install opencv-contrib-python-headless 
pip install opencv-python
python -c "import cv2"
sudo apt install libffi-dev
sudo pip3 install cffi
pip3 install jupyterlab
mkdir notebooks
jupyter lab --notebook-dir=~/notebooks
which jupyter-lab
/home/ai-class01/env/bin/jupyter-lab
</pre>
### Create a Service
sudo nano /etc/systemd/system/jupyter.service
### file:
<pre>
[Unit]
Description=Jupyter Lab
[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/bin/bash -c "/home/ai-class01/env/bin/jupyter-lab --ip="0.0.0.0" --no-browser --notebook-dir=/home/ai-class01/notebooks"
User=ai-class01
Group=ai-class01
WorkingDirectory=/home/ai-class01/notebooks
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
</pre>
###
<pre>
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service
sudo apt-get update && sudo apt-get install code
</pre>
##
#### Create password
* jupyter notebook --generate-config
* vi /home/ai-class01/.jupyter/jupyter_notebook_config.py
* jupyter notebook password
* edit .jupyter/jupyter_notebook_config.py
* change localhost to 0.0.0.0
* c.NotebookApp.ip = '0.0.0.0'
