import tkinter as tk
import psutil
import socket
import GPUtil

def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    cpu_info = f"external cores: {psutil.cpu_count(logical=False)}, internal cores: {psutil.cpu_count(logical=True)}"
    
    ram_info = f"total: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu_info = f"{gpus[0].name}, memory: {round(gpus[0].memoryTotal, 2)} MB"
    else:
        gpu_info = "no gpu found"
    
    return ip_address, cpu_info, ram_info, gpu_info

def display_system_info():
    ip_address, cpu_info, ram_info, gpu_info = get_system_info()
    
    lbl_ip.config(text=f"IPv4 Address: {ip_address}")
    lbl_cpu.config(text=f"CPU Info: {cpu_info}")
    lbl_ram.config(text=f"RAM Info: {ram_info}")
    lbl_gpu.config(text=f"GPU Info: {gpu_info}")

window = tk.Tk()
window.title("i love koldun")

lbl_ip = tk.Label(window, text="IPv4 Address: ", font=("Consolas", 12))
lbl_ip.pack(pady=5)

lbl_cpu = tk.Label(window, text="CPU Info: ", font=("Consolas", 12))
lbl_cpu.pack(pady=5)

lbl_ram = tk.Label(window, text="RAM Info: ", font=("Consolas", 12))
lbl_ram.pack(pady=5)

lbl_gpu = tk.Label(window, text="GPU Info: ", font=("Consolas", 12))
lbl_gpu.pack(pady=5)

btn_refresh = tk.Button(window, text="Refresh", command=display_system_info, font=("Consolas", 12))
btn_refresh.pack(pady=20)

display_system_info()
window.mainloop()
