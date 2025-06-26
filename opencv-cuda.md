🧱 環境前提
開發板：Jetson Orin Nano

系統版本：Ubuntu 20.04 or 22.04（JetPack 5.1 ~ 6.0）

CUDA：JetPack 自帶 (CUDA 11.x + cuDNN + TensorRT)

Python：建議使用 Python 3.8+（使用 Conda 或 venv）

🧰 第一步：安裝必要工具與依賴
bash
複製
編輯
sudo apt update
sudo apt upgrade -y

# 基本編譯工具與 OpenCV 依賴
sudo apt install -y \
    build-essential cmake git pkg-config libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
    gfortran openexr libatlas-base-dev python3-dev \
    python3-numpy libtbb2 libtbb-dev libdc1394-22-dev \
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
    libcanberra-gtk-module libcanberra-gtk3-module

# 建議安裝 Python 虛擬環境工具
sudo apt install -y python3-venv python3-pip
🌐 第二步：下載 OpenCV 原始碼（4.8.0）
bash
複製
編輯
mkdir -p ~/opencv_build && cd ~/opencv_build
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git

cd opencv
git checkout 4.8.0
cd ../opencv_contrib
git checkout 4.8.0
⚙️ 第三步：配置編譯（啟用 CUDA）
bash
複製
編輯
cd ~/opencv_build
mkdir -p build && cd build

cmake ../opencv \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
  -D ENABLE_NEON=ON \
  -D WITH_CUDA=ON \
  -D WITH_CUDNN=ON \
  -D OPENCV_DNN_CUDA=ON \
  -D CUDA_ARCH_BIN=8.7 \
  -D WITH_TBB=ON \
  -D WITH_V4L=ON \
  -D WITH_QT=OFF \
  -D WITH_OPENGL=ON \
  -D BUILD_opencv_python3=ON \
  -D BUILD_TESTS=OFF \
  -D BUILD_PERF_TESTS=OFF \
  -D BUILD_EXAMPLES=OFF \
  -D BUILD_opencv_world=OFF \
  -D PYTHON_EXECUTABLE=$(which python3) \
  -D INSTALL_PYTHON_EXAMPLES=ON
📌 備註：

CUDA_ARCH_BIN=8.7 適用於 Jetson Orin Nano（Ampere GA10B 架構）

可用 nvcc --list-gpu-arch 查詢支援的架構

🛠 第四步：開始編譯與安裝
Jetson Orin Nano 效能有限，建議：

bash
複製
編輯
# 使用所有 CPU 核心編譯（耗時 1.5~2 小時）
make -j$(nproc)

# 安裝
sudo make install
sudo ldconfig
🧪 第五步：驗證是否支援 CUDA
在 Python 中測試：

python
複製
編輯
import cv2
print("OpenCV version:", cv2.__version__)
print("CUDA available:", cv2.cuda.getCudaEnabledDeviceCount() > 0)
或在終端查看 OpenCV 組建資訊：

bash
複製
編輯
python3 -c "import cv2; print(cv2.getBuildInformation())" | grep -i CUDA
✅ 成功指標
cv2.__version__ 為 4.8.0

cv2.cuda.getCudaEnabledDeviceCount() 為 1 或更大

cv2.cuda.Sobel、cv2.cuda.GaussianBlur 等能成功執行

可使用 jtop 或 tegrastats 觀察 GPU 在影像處理時有活躍運作

🧼 （可選）移除預設舊版 OpenCV（避免衝突）
Jetson 預設版本可能在 /usr/lib/python3/dist-packages 中：

bash
複製
編輯
sudo find /usr/lib -name "*cv2*.so"
# 若無使用，建議移除
sudo apt remove python3-opencv
🧰 延伸補充
工具	用途
cv2.cuda.printShortCudaDeviceInfo(0)	顯示 GPU 設定
cv2.cuda.getCudaEnabledDeviceCount()	查詢 GPU 數量
cv2.cuda_GpuMat()	CUDA 版的圖像記憶體結構
Jetson 官方 Docker	若不想自行編譯，可使用 NVIDIA Container with OpenCV
