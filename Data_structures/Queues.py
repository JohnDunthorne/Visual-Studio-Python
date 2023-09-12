# queues are like stacks, but instead of FIFO first in first out
# queues are FIFO, first in first out

from collections import deque  # (pronounced dee-queue)

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

while queue:  # < this just mean while queue list has values
    queue.popleft()
    print(queue)
if not queue:  # , this means queue list has no values
    print("empty")
