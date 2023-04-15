import psutil
# More info https://psutil.readthedocs.io/en/latest
print("\nCPU info:")
# Number of CPU if logical=False = physical CPU
print(psutil.cpu_count(logical=False)) 
# current percentange of CPU is being used
print(psutil.cpu_percent(interval=1)) # interval in seconds
print(psutil.cpu_times())
print(psutil.cpu_stats())

# RAM
print("\nRAM info:")
print(psutil.virtual_memory())
RAM_availble=psutil.virtual_memory().available/(1024 ** 3)
RAM_total= psutil.virtual_memory().total/(1024 ** 3)
print(f"Available RAM: {round(RAM_availble,2)}GB")
print(f"Total RAM: {round(RAM_total,2)}GB")

# Hard Disc
print(psutil.disk_usage('/'))
disc_info_all=psutil.disk_usage('/')
disk_total=disc_info_all.total/(1024 ** 3)
disk_used=disc_info_all.used/(1024 ** 3)
disk_fee=disc_info_all.free/(1024 ** 3)
print(f"Available Memory: {round(disk_fee,2)}GB")
print(f"Total Memory: {round(disk_total,2)}GB")
print(f"Used Memory: {round(disk_used,2)}GB")
print(psutil.disk_partitions())