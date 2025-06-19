以下是為 **人工智能系老師** 設計的兩次各三小時的 **Jetson Orin Nano Super 培訓計畫課程大綱**。課程聚焦於實作與應用導向，協助教師理解硬體架構、軟體平台、AI部署流程與教學整合應用。

---

## 🧠 Jetson Orin Nano Super 培訓計畫（共 6 小時，分兩次）

### 🎯 對象

人工智能系教師，具備基本 Python、AI 理論背景，首次接觸 Jetson Orin 系列開發板。

### 🛠 硬體設備

每位學員配備 Jetson Orin Nano Super 開發套件（含電源、散熱、SD 卡），預先安裝好 JetPack SDK。

---

## 📅 第一天：**Jetson Orin Nano 環境與 AI 邊緣運算實作入門**

**時數：3 小時**

### 1. 課程導入（15 分鐘）

* Jetson 系列簡介（Nano → Xavier → Orin 系列）
* AI 邊緣運算的重要性與應用場景（智慧工廠、安防、醫療、交通）

### 2. 開發環境建置與介紹（45 分鐘）

* JetPack SDK 組成：Ubuntu + CUDA + TensorRT + DeepStream
* 系統初始化與遠端連接（SSH/VNC）
* 使用 `jtop`/`tegrastats` 觀察資源

### 3. AI 部署流程概念（30 分鐘）

* PyTorch/TensorFlow 模型轉換 → ONNX → TensorRT 加速
* 邊緣 vs 雲端推論比較
* 實作演練簡介：貓狗分類/YOLOv8影像辨識

### 4. 範例實作：影像分類（60 分鐘）

* 使用 PyTorch 訓練好的模型
* 模型轉換為 ONNX，部署到 Jetson
* 利用 Python + OpenCV 播放攝影機，執行即時分類

### 5. 工具與部署技巧（30 分鐘）

* 使用 `TensorRT` 加速 ONNX 模型
* 使用 Docker 管理 AI 應用
* 模型部署效能比較（CPU vs GPU vs TensorRT）

### 🧪 作業建議：

* 嘗試自行訓練簡單模型，轉成 ONNX 並部署至 Jetson
* 準備一張 USB 攝影機 + 影像資料集

---

## 📅 第二天：**進階應用：物件偵測、深度串流與多模型整合**

**時數：3 小時**

### 1. 物件偵測模型部署：YOLOv8（60 分鐘）

* 下載預訓練 YOLOv8 模型
* 模型轉 ONNX → TensorRT
* 透過 OpenCV + YOLOv8 實作即時物件偵測（USB/CSI 攝影機）

### 2. 多路視訊串流整合（30 分鐘）

* CSI+USB 雙鏡頭支援
* 使用 `GStreamer` 建構影像串流與硬體加速流程

### 3. DeepStream SDK 入門（30 分鐘）

* NVIDIA DeepStream 架構簡介（多攝影機、事件驅動）
* 使用預設 pipeline 快速展示物件偵測與分析

### 4. 教學與專題整合應用探討（30 分鐘）

* 如何將 Jetson 平台應用於課堂專案
* 推薦主題：智慧交通車流辨識、教室人數統計、自動化檢測
* 評估 TensorRT/DeepStream 效能回饋

### 5. 實作演練：部署多模型任務（30 分鐘）

* 同時執行人臉辨識 + 手勢辨識
* 資源配置與優化（GPU 時脈、CUDA stream）

---

## 📘 附錄：教學資源包建議

* NVIDIA 官方：Jetson AI Fundamentals 課程
* [NVIDIA Jetson Zoo](https://elinux.org/Jetson_Zoo)：各類開源專案連結
* [NGC Catalog](https://ngc.nvidia.com/): 預訓練模型與容器支援
* Colab → Jetson 的模型遷移範例

---

如需，我可以將此大綱轉為 Word / PDF / PPT 格式或延伸設計一份學習手冊。是否需要？
