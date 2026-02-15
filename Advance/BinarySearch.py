nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter number to search: "))

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print("Found at index", mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")
