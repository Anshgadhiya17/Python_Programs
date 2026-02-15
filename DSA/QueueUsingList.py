queue = []

n = int(input("How many elements to enqueue: "))

for _ in range(n):
    queue.append(int(input("Enter element: ")))

print("Queue:", queue)

if queue:
    print("Dequeued:", queue.pop(0))

print("After Dequeue:", queue)
