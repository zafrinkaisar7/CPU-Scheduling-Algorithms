# SJF Scheduling

n = int(input("Enter number of processes: "))
process_data = []

for i in range(n):
    pname = input(f"Enter name of process {i+1}: ")
    bt = int(input(f"Enter burst time for {pname}: "))
    process_data.append((pname, bt))

# Sort by burst time
process_data.sort(key=lambda x: x[1])

waiting_time = {}
start_time = 0
total_waiting_time = 0

# Gantt chart output
print("\nGantt Chart:")
for pname, bt in process_data:
    print(f"{start_time} {pname}", end=" ")
    waiting_time[pname] = start_time
    start_time += bt
print(start_time)

# Average waiting time
avg_wt = sum(waiting_time[p] for p, _ in process_data) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f} ms")