nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter number to search: "))

for i in range(len(nums)):
    if nums[i] == target:
        print("Found at index", i)
        break
else:
    print("Not Found")
