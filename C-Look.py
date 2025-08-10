requests = [98, 183, 37, 122, 14, 124, 65, 67]
start = 53
path = [start]
total_distance = 0

# Sort the queue
requests.sort()

# Split into left and right of head
left = [r for r in requests if r <= start]
right = [r for r in requests if r > start]

head = start

# Move right (greater than head)
for req in right:
    total_distance += abs(head - req)
    head = req
    path.append(head)

# Jump to the smallest request (left side)
for req in left:
    total_distance += abs(head - req)
    head = req
    path.append(head)

# Output
print('path:', path)
print(f'Total Head Movement: {total_distance} cylinders')
