https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit
nvcc -V
vim ~/.bashrc              #如果出現 bash: nvcc: command not found ，請添加環境變數：
#在結尾添加：
```
export LD_LIBRARY_PATH=/usr/local/cuda/lib export PATH=$PATH:/usr/local/cuda/bin
export PATH=$PATH:/usr/local/cuda/bin
```
==
```
source ~/.bashrc
```
## cuDNN
```
dpkg -l libcudnn8
```
## TensorRT
```
dpkg -l | grep nvinfer
```
#三、安裝 Tensorflow
## 3.1 安裝 Tensorflow 所需套件
```
sudo apt-get update
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
```
## 3.2 更新 python 中的 pip
```
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip
sudo pip3 install -U testresources setuptools==65.5.0
```
## 3.3 安裝 python 相關套件
```
sudo pip3 install -U numpy==1.22 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig packaging h5py==3.6.0
```
## 3.4 安裝 tensorflow
### 下方指令的環境為 JetPack 5.1.2
```
sudo pip3 install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v512 tensorflow==2.12.0+nv23.06
```
### 如須用其他版本請使用下方指令
```
sudo pip3 install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v$JP_VERSION tensorflow==$TF_VERSION+nv$NV_VERSION
```
## 3.5 驗證是否安裝成功
```
python3 --version
```
## Import TensorFlow:
```
python3 -c "import tensorflow as tf;print(tf.__version__)"
```
# 四、安裝 pytorch
## 4.1 安裝 pytorch 所需套件
```
sudo apt-get -y update; 
sudo apt-get -y install autoconf bc build-essential g++-8 gcc-8 clang-8 lld-8 gettext-base gfortran-8 iputils-ping libbz2-dev libc++-dev libcgal-dev libffi-dev libfreetype6-dev libhdf5-dev libjpeg-dev liblzma-dev libncurses5-dev libncursesw5-dev libpng-dev libreadline-dev libssl-dev libsqlite3-dev libxml2-dev libxslt-dev locales moreutils openssl python-openssl rsync scons python3-pip libopenblas-dev;
```
## 4.2 export pytorch 安裝連結
```
export TORCH_INSTALL=https://developer.download.nvidia.cn/compute/redist/jp/v511/pytorch/torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64.whl
```
## 4.3 安裝 pytorch
```
python3 -m pip install --upgrade pip; python3 -m pip install aiohttp numpy=='1.19.4' scipy=='1.5.3' export "LD_LIBRARY_PATH=/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH"; python3 -m pip install --upgrade protobuf; python3 -m pip install --no-cache $TORCH_INSTALL
```
## 4.4 安裝 torchvision
## torchvision 與 pytorch 要對應，需先上網找尋互相支援版本
```
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
git clone --branch <version> https://github.com/pytorch/vision torchvision   # <version> = v0.15.0; for PyTorch==2.0.0

$ git clone --branch release/0.15 https://github.com/pytorch/vision torchvision
$ cd torchvision
$ export BUILD_VERSION=0.15.0  # where 15 could be ohter torchvision versions
$ python3 setup.py install --user
$ cd ../  # attempting to load torchvision from build dir will result in import error
$ pip3 install --upgrade pillow
```
## 4.5 驗證安裝
```
$ export LD_LIBRARY_PATH=/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH
$ python3
```
## 導入 PyTorch：
```
>>> import torch
>>> import torchvision
```
# 五、 OpenCV 4.8.0 安裝
## 因為原本內建的 OpenCV 並沒有支援 CUDA，所以需要 Build 一版出來進行安裝

## 5.1 先刪除原本內建的 OpenCV
```
sudo sudo apt-get purge *libopencv*
```
## 5.2 執行 OpenCV sh檔案
### CUDA_ARCH_BIN=8.7 需要事先找出版本
### 可先用 5.3 方法先安裝 jtop
## 將下方程式複製到文件轉成.sh檔
```
#!/bin/bash
set -e

echo "Installing OpenCV 4.8.0 on your Jetson Nano"

# reveal the CUDA location
cd ~
sudo sh -c "echo '/usr/local/cuda/lib64' >> /etc/ld.so.conf.d/nvidia-tegra.conf"
sudo ldconfig

# install the dependencies
sudo apt-get install -y build-essential cmake git unzip pkg-config zlib1g-dev
sudo apt-get install -y libjpeg-dev libjpeg8-dev libjpeg-turbo8-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libglew-dev
sudo apt-get install -y libgtk2.0-dev libgtk-3-dev libcanberra-gtk*
sudo apt-get install -y python3-dev python3-numpy python3-pip
sudo apt-get install -y libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install -y libtbb2 libtbb-dev libdc1394-22-dev libxine2-dev
sudo apt-get install -y gstreamer1.0-tools libv4l-dev v4l-utils qv4l2 
sudo apt-get install -y libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev
sudo apt-get install -y libavresample-dev libvorbis-dev libxine2-dev libtesseract-dev
sudo apt-get install -y libfaac-dev libmp3lame-dev libtheora-dev libpostproc-dev
sudo apt-get install -y libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install -y libopenblas-dev libatlas-base-dev libblas-dev
sudo apt-get install -y liblapack-dev liblapacke-dev libeigen3-dev gfortran
sudo apt-get install -y libhdf5-dev protobuf-compiler
sudo apt-get install -y libprotobuf-dev libgoogle-glog-dev libgflags-dev

# remove old versions or previous builds
cd ~ 
sudo rm -rf opencv*
# download the latest version
git clone --depth=1 https://github.com/opencv/opencv.git
git clone --depth=1 https://github.com/opencv/opencv_contrib.git

# set install dir
cd ~/opencv
mkdir build
cd build

# run cmake
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
-D WITH_OPENCL=OFF \
-D WITH_CUDA=ON \
-D CUDA_ARCH_BIN=8.7 \
-D CUDA_ARCH_PTX="" \
-D WITH_CUDNN=ON \
-D WITH_CUBLAS=ON \
-D ENABLE_FAST_MATH=ON \
-D CUDA_FAST_MATH=ON \
-D OPENCV_DNN_CUDA=ON \
-D ENABLE_NEON=ON \
-D WITH_QT=OFF \
-D WITH_OPENMP=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_GSTREAMER=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=ON \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D WITH_PROTOBUF=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D BUILD_EXAMPLES=OFF ..

# run make

make -j 

sudo make install
sudo ldconfig

# cleaning (frees 320 MB)
make clean
sudo apt-get update

echo "Congratulations!"
echo "You've successfully installed OpenCV 4.8.0 on your Jetson Nano"
```
## 依照剛剛所儲存的名稱{name} 加入權限，並執行
```
$ sudo chmod 755 ./{name}.sh #路徑請依照自己sh檔位置執行
$ ./{name}.sh
```
## 5.3 檢查是否成功安裝 OpenCV ( CUDA 版本)
```
$ sudo pip3 install jetson-stats
$ sudo reboot 
$ jtop
```