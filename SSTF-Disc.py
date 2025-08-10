queue = [98,183,37,122,14,124,65,67]
path = []
head_start_pointer = 53
path.append(head_start_pointer)
total_distance = 0

for i in range(len(queue)):
  minimum_distance = float('inf')
  index = -1

  for i in range(len(queue)):
    distance = abs(head_start_pointer-queue[i])

    if distance < minimum_distance:
      minimum_distance = distance
      index = i

  path.append(queue[index])
  head_start_pointer = queue[index]
  total_distance = total_distance + minimum_distance
  queue.pop(index)



print('path:',path)
print(f'Total Head Movement: {total_distance} cylinders')