# Initial setup
queue = [98, 183, 37, 122, 14, 124, 65, 67]
start = 53
disk_start = 0
disk_end = 199

# Sort the queue
queue.sort()

# Separate requests to the left and right of head
left = [req for req in queue if req <= start]
right = [req for req in queue if req > start]

# Add disk ends
left.append(disk_start)
right.append(disk_end)

# Sort both sides
left.sort()
right.sort()

# CSCAN Scheduling
path = [start]
head = start
total_distance = 0

# Move right
for req in right:
    total_distance += abs(head - req)
    head = req
    path.append(head)

# Move from end (199) to start (0)
for req in left:
    total_distance += abs(head - req)
    head = req
    path.append(head)

# Output
print('path:', path)
print(f'Total Head Movement: {total_distance} cylinders')
