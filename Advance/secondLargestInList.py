nums = list(map(int, input("Enter numbers separated by space: ").split()))

nums = list(set(nums))
nums.sort()

if len(nums) >= 2:
    print("Second Largest:", nums[-2])
else:
    print("Not enough elements")
