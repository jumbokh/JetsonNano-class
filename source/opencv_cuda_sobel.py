import cv2, time

cap = cv2.VideoCapture(0)  # USB 攝影機
assert cap.isOpened(), "Camera not found"

gpu_available = cv2.cuda.getCudaEnabledDeviceCount() > 0
print("OpenCV CUDA available:", gpu_available)

# Sobel 核心
def sobel_cpu(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)

def sobel_gpu(frame):
    gpu_frame = cv2.cuda_GpuMat()
    gpu_frame.upload(frame)
    gray = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2GRAY)
    sobel = cv2.cuda.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
    return sobel.download()

mode_gpu = gpu_available
t_prev, cnt = time.time(), 0

while True:
    ret, frame = cap.read()
    if not ret: break
    output = sobel_gpu(frame) if mode_gpu else sobel_cpu(frame)
    cv2.imshow("Sobel", output)
    cnt += 1
    if time.time() - t_prev > 1:              # 每秒統計 FPS
        print("GPU" if mode_gpu else "CPU", "FPS:", cnt)
        cnt, t_prev = 0, time.time()
    key = cv2.waitKey(1) & 0xFF
    if key == ord('m'): mode_gpu = not mode_gpu  # m 鍵切換
    if key == 27: break                         # ESC 離開

cap.release()
cv2.destroyAllWindows()
