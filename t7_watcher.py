import psutil
import time
import re

def is_process_running(process_name_pattern):
    for proc in psutil.process_iter(attrs=['name']):
        try:
            if re.match(process_name_pattern, proc.info['name'], re.IGNORECASE):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def terminate_process(process_name):
    for proc in psutil.process_iter(attrs=['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                proc.terminate()
                print(f"Terminated process: {process_name}")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"Failed to terminate process: {process_name}")
    return False

def monitor_processes():
    t7_patch_pattern = r"t7patch_\d+\.\d+\.exe"

    while True:
        try:
            if is_process_running(r"BlackOps3.exe") and not is_process_running(t7_patch_pattern):
                print("BlackOps3.exe is running, but T7 patch is not running. Terminating BlackOps3.exe...")
                terminate_process("BlackOps3.exe")
            
            time.sleep(5)

        except Exception as e:
            print(f"Error occurred: {e}")
            break

if __name__ == "__main__":
    print("Script started")
    monitor_processes()