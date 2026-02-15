nums = list(map(int, input("Enter numbers separated by space: ").split()))

is_sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("List is Sorted")
else:
    print("List is Not Sorted")
