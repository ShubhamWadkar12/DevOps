a = int(input("Enter first number"))
b = int(input("Enter second number"))
print("The sum of a and b is:", a + b)
print("The product of a and b is:", a * b)
print("The difference of a and b is:", a - b)
print("The division of a and b is:", a / b)

------------------------------------------------

import psutil
def check_cpu_usage():
    cpu_limit = int(input("Enter CPU usage limit : "))
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {cpu_usage}%")
    if cpu_usage > cpu_limit:
        print("High CPU usage detected! ❌")
    else:
        print("CPU normal ✅")
check_cpu_usage()
