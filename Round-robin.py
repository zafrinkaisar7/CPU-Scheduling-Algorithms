process_dict = {
    'pros': ['p1', 'p2', 'p3', 'p4'],
    'burst_time': [21, 3, 6, 2]
}

completion_time = [0] * len(process_dict['pros'])
waiting_time = 0
quantum = 5
time = 0
print(time, end='')

while True:
    if sum(process_dict['burst_time']) == 0:
        break

    count = -1
    for i in process_dict['burst_time']:
        count += 1

        if process_dict['burst_time'][count] == 0:
            continue

        if process_dict['burst_time'][count] < quantum:
            time += process_dict['burst_time'][count]
            print(f'{process_dict["pros"][count]} {time}', end='')
            process_dict['burst_time'][count] = 0
            completion_time[count] = time
        else:
            time += quantum
            print(f'{process_dict["pros"][count]} {time}', end='')
            process_dict['burst_time'][count] -= quantum


orginal_burst_time = process_dict['burst_time']


waiting_times = []
for i in range(len(orginal_burst_time)):
    wt = completion_time[i] - orginal_burst_time[i]
    waiting_times.append(wt)

avg_waiting_time = sum(waiting_times) / len(waiting_times)

print("\nWaiting times:", waiting_times)
print("Average waiting time:", avg_waiting_time)