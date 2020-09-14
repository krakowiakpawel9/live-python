import psutil


for proc in psutil.process_iter():
    try:
        process_name = proc.name()
        process_id = proc.pid
        print(f'{process_name} : {process_id}')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
