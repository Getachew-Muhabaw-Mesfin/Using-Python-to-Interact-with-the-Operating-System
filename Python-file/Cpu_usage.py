import psutil

cpuPercent =psutil.cpu_percent(0.5)
logical_cpu= psutil.cpu_count(logical=True)
physical_cpu =psutil.cpu_count(logical=False)
cpu_freq = psutil.cpu_freq(percpu=False)
cpu_statics= psutil.cpu_stats()
ctx_switchs= cpu_statics.ctx_switches
inter= cpu_statics.interrupts
softInterp =cpu_statics.soft_interrupts
system_calls =cpu_statics.syscalls
cpu_time=psutil.cpu_times(percpu=False)
cpu_time_for_each_cpu= psutil.cpu_times(percpu=True)
print(f'Number of Logical CPU in the System is : {logical_cpu}')
print(f'Number of Physical CPU in the System is : {physical_cpu}')
print(f'CPU Frequencay:{cpu_freq}')
print(f'CPU Statstics : {cpu_statics}')
print(f'CTX-Switches: {ctx_switchs}')
print(f'System interrupts: {inter}')
print(f'Software Interrupts: {softInterp}')
print(f'System Calls :{system_calls}')
print(f'CPU time: {cpu_time}')
print(f'CPU times for each CPU {len(cpu_time_for_each_cpu)} CPUS: {cpu_time_for_each_cpu}')
print(f'Avrage Cpu usege in 0.5 second is :{cpuPercent}') ## cpu usage in 0.1 second so it is variable


