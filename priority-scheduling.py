process_dict = {
    'pros': ['p1', 'p2', 'p3', 'p4'],
    'burst_time': [21, 3, 6, 2],
    'priority': [2, 1, 4, 3]
}

prio = 1
waiting_time = 0
storing_waiting_time = []

# Use a list to build formatted output
output_parts = [str(waiting_time)]

for i in process_dict['priority']:
    for index, priority in enumerate(process_dict['priority']):
        if priority == prio:
            waiting_time += process_dict['burst_time'][index]
            storing_waiting_time.append(waiting_time)
            # Append formatted string with space separator
            output_parts.append(f"{process_dict['pros'][index]} {waiting_time}")
            prio += 1
            break

# Join the parts with spaces
formatted_output = ' '.join(output_parts)
print(formatted_output)

# Calculate average waiting time (excluding last process's waiting time)
average_waiting_time = sum(storing_waiting_time[:-1]) / len(process_dict['pros'])
print(f'Average Waiting Time: {average_waiting_time}')