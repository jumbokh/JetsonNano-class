

## 🎯 教學目標

* 在 Jetson Orin Nano 上建置 YOLOv5 運行環境
* 完成預訓練模型下載與推論測試（圖片 / 攝影機）
* 確認 GPU CUDA 加速正常運行

---

## ✅ 一、系統環境與依賴說明

| 項目           | 說明                                      |
| ------------ | --------------------------------------- |
| 作業系統         | Ubuntu 20.04 / 22.04（JetPack 5.x / 6.x） |
| CUDA / cuDNN | JetPack 已預裝                             |
| Python       | 建議使用 Python 3.8+                        |
| PyTorch      | NVIDIA 提供 Jetson 專用版本                   |
| OpenCV       | 建議自行安裝支援 CUDA 的版本（可參考前面步驟）              |

---

## 🧰 二、YOLOv5 安裝步驟

### 1. 更新系統並安裝依賴

```bash
sudo apt update
sudo apt install -y git python3-pip python3-venv libopencv-dev
```

### 2. 建立虛擬環境（建議）

```bash
python3 -m venv yolov5-env
source yolov5-env/bin/activate
```

### 3. 下載 YOLOv5 原始碼

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
```

### 4. 安裝相依套件（Jetson 較特殊）

建議手動安裝 NVIDIA 版本的 PyTorch（以 JetPack 5.1.1 為例）：

```bash
# 若尚未安裝 PyTorch：
pip3 install torch==1.13.0+nv22.10 torchvision==0.14.0+nv22.10 -f https://developer.download.nvidia.com/compute/redist/jp/v511

# 安裝 YOLOv5 相依項目
pip install -r requirements.txt
```

> 若使用 JetPack 6.0，則需搭配 `torch==2.1.0+nv23.06`，請根據實際版本對應。

---

## 🧪 三、測試 YOLOv5 推論

### 1. 測試圖片推論（預設模型）

```bash
python detect.py --weights yolov5s.pt --source data/images/bus.jpg --device 0
```

若成功，會產生 `runs/detect/exp/` 資料夾，裡面為標註過的輸出圖像。

### 2. 測試即時 USB 攝影機

```bash
python detect.py --weights yolov5s.pt --source 0 --device 0
```

或使用 CSI 攝影機（如 Raspberry Pi Camera）：

```bash
python detect.py --weights yolov5s.pt --source 0 --device 0 --img 640
```

### 3. 確認 GPU 是否啟用

在程式中加上：

```python
import torch
print("CUDA:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))
```

或執行時確認 `--device 0` 使用 GPU，而非 `cpu`。

---

## ⚙️ 四、改善效能（可選）

| 技術                          | 效果        | 操作建議        |
| --------------------------- | --------- | ----------- |
| `--img 640` → `--img 320`   | 降低解析度加快速度 | 減少處理負擔      |
| `yolov5s.pt` → `yolov5n.pt` | 使用更輕量模型   | 損失精度但更快     |
| TensorRT                    | 將模型加速     | 可進一步導入（見延伸） |

---

## 🧱 五、常見問題排解

| 問題                        | 解法                                                |
| ------------------------- | ------------------------------------------------- |
| `ImportError: libGL.so.1` | `sudo apt install libgl1`                         |
| 沒有 GPU                    | 確認 JetPack 安裝完整，使用 `torch.cuda.is_available()` 檢查 |
| 執行很慢                      | 改用 `yolov5n.pt` 或降低影像尺寸                           |
| `cv2.error`               | 安裝不完整 OpenCV，請重新編譯支援 CUDA 版本                      |

---

## 📦 六、延伸：轉換為 TensorRT 加速（可選）

1. 安裝 [ultralytics/yolov5](https://github.com/ultralytics/yolov5) 的 ONNX export 功能：

```bash
python export.py --weights yolov5s.pt --include onnx
```

2. 將 ONNX 模型轉為 TensorRT：

```bash
/usr/src/tensorrt/bin/trtexec --onnx=yolov5s.onnx --saveEngine=yolov5s.engine --fp16
```

3. 使用 `tensorrt-python` 呼叫 `.engine` 檔做推論（需額外撰寫 C++ 或 Python 呼叫程式）。

---

## ✅ 成功標準檢查表

* [x] `detect.py` 成功執行，推論結果儲存在 `runs/detect/exp`
* [x] `torch.cuda.is_available()` 為 True
* [x] 使用 CSI 或 USB 攝影機可即時推論（FPS > 10）
* [x] 模型大小可自選（n/s/m/l/x）

---

## 📄 附加資源

* [Jetson Zoo - 深度學習專案整理](https://elinux.org/Jetson_Zoo)
* [NVIDIA 官方 PyTorch 版本對應表](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
* [Ultralytics YOLOv5 GitHub](https://github.com/ultralytics/yolov5)


