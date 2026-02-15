stack = []

n = int(input("How many elements to push: "))

for _ in range(n):
    stack.append(int(input("Enter element: ")))

print("Stack:", stack)

if stack:
    print("Popped:", stack.pop())

print("After Pop:", stack)
