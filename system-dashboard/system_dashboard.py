import platform
import shutil
import psutil

print("=" * 50)
print(" Professional System Information Dashboard ")
print("=" * 50)

print(f"Operating System : {platform.system()}")
print(f"OS Version       : {platform.release()}")
print(f"Machine          : {platform.machine()}")
print(f"Processor        : {platform.processor()}")

print("\nMemory")
memory = psutil.virtual_memory()
print(f"Total RAM        : {memory.total / (1024**3):.2f} GB")
print(f"Available RAM    : {memory.available / (1024**3):.2f} GB")
print(f"RAM Usage        : {memory.percent}%")

print("\nStorage")
disk = shutil.disk_usage("/")
print(f"Total Storage    : {disk.total / (1024**3):.2f} GB")
print(f"Used Storage     : {disk.used / (1024**3):.2f} GB")
print(f"Free Storage     : {disk.free / (1024**3):.2f} GB")

print("\nCPU")

try:
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage        : {cpu}%")
except PermissionError:
    print("CPU Usage        : Not available (Android restriction)")
except Exception as e:
    print(f"CPU Usage        : Error: {e}")

print("\nNetwork")

try:
    net = psutil.net_io_counters()
    print(f"Bytes Sent       : {net.bytes_sent}")
    print(f"Bytes Received   : {net.bytes_recv}")
except PermissionError:
    print("Network Stats    : Permission denied")
except Exception as e:
    print(f"Network Stats    : Error: {e}")

print("\nDashboard Complete!")
