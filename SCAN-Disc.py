queue = [98,183,37,122,14,124,65,67]
queue.sort()
path = []
head_start_pointer = 53
path.append(head_start_pointer)
total_distance = 0
left_queue = []
right_queue = []

disk_start = 0
disk_end = 199

# spliting queue into left to right queue
for i in range(len(queue)):
  if queue[i] <= head_start_pointer:
    left_queue.append(queue[i])

  else:
    right_queue.append(queue[i])

left_queue.append(disk_start)
left_queue.sort(reverse= True)


for i in range(len(left_queue)):
  total_distance = total_distance + abs(head_start_pointer - left_queue[i])
  head_start_pointer=left_queue[i]
  path.append(left_queue[i])

for i in range(len(right_queue)):
  total_distance = total_distance + abs(head_start_pointer - right_queue[i])
  head_start_pointer=right_queue[i]
  path.append(right_queue[i])

print('path:',path)
print(f'Total Head Movement: {total_distance} cylinders')
