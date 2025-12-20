import psutil

def check_cpu_usage():

    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > 75:
        print("High CPU usage detected! ❌")
    else:
        print("CPU normal ✅")

check_cpu_usage()