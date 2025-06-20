#
# pip3 install --upgrade torch torchvision --extra-index-url https://download.pytorch.org/whl/cu118
# python3 -c "import torch, platform, os; print(torch.__version__, torch.version.cuda)"
#
import torch, time

device_cpu = torch.device('cpu')
device_gpu = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

print("CUDA Available:", torch.cuda.is_available())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")

# 4096x4096 矩陣
N = 4096
A = torch.randn(N, N)
B = torch.randn(N, N)

def matmul_test(device):
    A_d, B_d = A.to(device), B.to(device)
    torch.cuda.synchronize() if device.type == 'cuda' else None
    t0 = time.perf_counter()
    C = A_d @ B_d
    torch.cuda.synchronize() if device.type == 'cuda' else None
    t1 = time.perf_counter()
    return t1 - t0

cpu_time = matmul_test(device_cpu)
gpu_time = matmul_test(device_gpu)

print(f"CPU time: {cpu_time:.4f}s")
print(f"GPU time: {gpu_time:.4f}s")
print(f"Speed-up: {cpu_time/gpu_time:.2f}×")
