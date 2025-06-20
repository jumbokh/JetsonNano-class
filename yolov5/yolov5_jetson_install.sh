#!/bin/bash
# YOLOv5 Jetson Orin Nano 自動安裝腳本

echo "✅ 更新系統"
sudo apt update && sudo apt install -y git python3-pip python3-venv libopencv-dev

echo "✅ 建立 Python 虛擬環境"
python3 -m venv yolov5-env
source yolov5-env/bin/activate

echo "✅ 下載 YOLOv5 原始碼"
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

echo "✅ 安裝 NVIDIA PyTorch（JetPack 5.x 範例）"
pip install torch==1.13.0+nv22.10 torchvision==0.14.0+nv22.10 -f https://developer.download.nvidia.com/compute/redist/jp/v511

echo "✅ 安裝 YOLOv5 所需套件"
pip install -r requirements.txt

echo "✅ 測試圖片推論"
python detect.py --weights yolov5s.pt --source data/images/bus.jpg --device 0
