queue = [98,183,37,122,14,124,65,67]
path = []
head_start_pointer = 53
path.append(head_start_pointer)
total_dist = 0

for i in range(len(queue)):
  path.append(queue[i])
  total_dist = total_dist + abs(head_start_pointer - queue[i])
  head_start_pointer = queue[i]

print('path:',path)
print(f'Total Head Movement: {total_dist} cylinders')
