# JetPack 5.x 內建 OpenCV + CUDA；若自行編譯需開啟 WITH_CUDA=ON
python3 - <<'PY'
import cv2
print("CUDA support:", cv2.cuda.getCudaEnabledDeviceCount() > 0)
print(cv2.getBuildInformation().split("Parallel framework")[0])
PY
