# FCFS Scheduling

n = int(input("Enter number of processes: "))
processes = []
burst_time = []

for i in range(n):
    pname = input(f"Enter name of process {i+1}: ")
    bt = int(input(f"Enter burst time for {pname}: "))
    processes.append(pname)
    burst_time.append(bt)

waiting_time = []
start_time = 0
total_waiting_time = 0

# Gantt chart output
print("\nGantt Chart:")
for i in range(n):
    print(f"{start_time} {processes[i]}", end=" ")
    waiting_time.append(start_time)
    start_time += burst_time[i]
print(start_time)

# Average waiting time
avg_wt = sum(waiting_time) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f} ms")