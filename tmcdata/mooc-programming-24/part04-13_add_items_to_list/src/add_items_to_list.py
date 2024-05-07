# Write your solution here
nums = []

count = int(input("How many items: "))

for i in range(1, count+1):
    nums.append(int(input(f"Item {i}: ")))
print(nums)